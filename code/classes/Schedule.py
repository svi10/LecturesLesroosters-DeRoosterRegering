from tokenize import String
import pandas as pd
import math
from typing import List, Set, Dict, Tuple, Optional

from code.classes.course import Course
from . import Roomslot, Student
from . import activity, course
from code import helpers


class Schedule:
    """
    This class can be used to devide the courses over the 
    roomslots (room-timeslot pair)
    """

    def __init__(self):
        self._courses_df = helpers.import_data("vakken")
        self._courses = {}
        self.make_courses()

        self._rooms_df = helpers.import_data("zalen")

        self._students_df = helpers.import_data("studenten_en_vakken")
        self.add_students_to_courses("Lineaire Algebra")

        self._students = self.student_list()
        self._activities = self.activity_list()
        self._roomslots = []
        room_ids = self.room_ids()
        room_capacities = self.room_capacities()
        largest_room_ID = self._rooms_df['Zaalnummber'].iloc[-1]
        largest_room_capacity = self._rooms_df['Max. capaciteit'].iloc[-1]

        # Make for every room in every timeslot a roomslot (there are 4*5=20 timeslots). Largest room has an extra timeslot (17-19u every day, so +5 timeslots)
        for timeslot in range(0, 25):
            # Make roomslots for largest room, 17-19u every day
            if  (timeslot + 1) % 5 == 0:
                roomslot = Roomslot.Roomslot(largest_room_ID, timeslot, largest_room_capacity)
                self._roomslots.append(roomslot)
            else:
                for roomID, capacity in zip(room_ids, room_capacities):
                    roomslot = Roomslot.Roomslot(roomID, timeslot, capacity)
                    self._roomslots.append(roomslot)
        self.sort_roomslots()


    def make_courses(self):
        """
        Make a dictionary of course objects for each course in the Course DataFrame
        """
        for row in self._courses_df.iterrows():
            self._courses[row[1]["Vak"]] = Course(row[1])


    def add_students_to_courses(self, course):
        selected_students = self._students_df[(self._students_df["Vak1"] == f"{course}") | 
                                              (self._students_df["Vak2"] == f"{course}") |
                                              (self._students_df["Vak3"] == f"{course}") |
                                              (self._students_df["Vak4"] == f"{course}") |
                                              (self._students_df["Vak5"] == f"{course}") ]

        student_list = selected_students["Stud. Nr."].tolist()
        print(student_list)
        print(f"Number of students {len(student_list)}")


    def sort_roomslots(self):
        """
        Sort the roomslots by capacity (largest -> smallest)
        """
        roomslot_tuple = []
        # Make list of tuples of the roomslots [(Capacity, Roomslot), (Capacity, Roomslot)]
        for roomslot in self._roomslots:
            roomslot_tuple.append((roomslot._capacity, roomslot))
        
        # Sort dictionary on capacity
        sorted_list = sorted(roomslot_tuple, key=lambda tup: tup[0])

        # Make list of sorted roomslots
        self._roomslots = []
        for item in sorted_list:
            self._roomslots.append(item[1])


    def room_ids(self) -> list:
        """Make list of all room ids"""
        return self._rooms_df['Zaalnummber'].tolist()


    def room_capacities(self) -> list:
        """Make list of all room capacities"""
        return self._rooms_df['Max. capaciteit'].tolist()


    def activity_list(self):
        """
        Make a list of all possible activities with the number of expected 
        participants.
        
        Example:
            
        [['Hoorcollege Advanced Heuristics', 22], 
         ['Practicum Advanced Heuristics', 22], 
         ['Hoorcollege Algoritmen en complexiteit', 47], 
         ['Werkcollege Algoritmen en complexiteit', 47],
         ...
         ]
        """
        activities = []

        for row in self._courses_df.iterrows():
            # Name of the course
            vak = row[1]['Vak']
            # Number of lectures, practicals and tutorials
            N_lectures = row[1]["#Hoorcolleges"]
            N_practicals = row[1]["#Practica"]
            max_students_practicum = row[1]["Max. stud. Practicum"]
            N_tutorials = row[1]["#Werkcolleges"]
            max_students_tutorials = row[1]["Max. stud. Werkcollege"]
            N_students = row[1]["Verwacht"]
             
            for i in range(N_lectures):
                activity = {}
                activity['Activity'] = "Hoorcollege " + vak
                activity['Verwacht'] = row[1]['Verwacht']
                activities.append(activity)
            
            for i in range(N_tutorials):
                N_groups = math.ceil(row[1]['Verwacht'] / int(row[1]['Max. stud. Werkcollege']))

                for group in range(N_groups):
                    activity = {}
                    activity['Activity'] = "Werkcollege " + vak + '.' + (str(group))
                    activity['Verwacht'] = row[1]['Verwacht']
                    activity['Max. stud. Werkcollege'] = row[1]['Max. stud. Werkcollege']
                    activities.append(activity)
            
            for i in range(N_practicals):
                N_groups = math.ceil(row[1]['Verwacht'] / int(row[1]['Max. stud. Practicum']))

                for group in range(N_groups):
                    activity = {}
                    activity['Activity'] = "Practicum " + vak + '.' + (str(group))
                    activity['Verwacht'] = row[1]['Verwacht']
                    activity['Max. stud. Practicum'] = row[1]['Max. stud. Practicum']
                    activities.append(activity)

        return activities
        

    def make_schedule(self) -> None:
        """
        Add all activities to a different timeslot
        """
        # Add all activities to the schedule
        for activity in self._activities: 
            self.add_to_schedule(activity)
    

    def add_to_schedule(self, activity: Dict[str, int]):
        """
        Add activity to the next possible room based on capacity
        """
        N_students = activity['Verwacht']
        # Find an available room for the activity
        for roomslot in self._roomslots:
            # Check if room available and has the right capacity
            if roomslot._activity == 'Available' and roomslot._capacity >= N_students:
                # Asign activity to roomslot
                roomslot.assign_activity(activity['Activity'])
                # Save number of students in the room
                roomslot._N_participants = N_students
                # Stop searching for an available room
                break
        

    def show_schedule(self):
        """
        Show schedule in a dataframe
        """
        timeslots = []
        rooms = []
        activities = []
        capacities = []
        N_students = []
    
        for roomslot in self._roomslots:
            timeslots.append(roomslot._timeslot)
            rooms.append(roomslot._roomID)
            activities.append(roomslot._activity)
            capacities.append(roomslot._capacity)
            N_students.append(roomslot._N_participants)

        data = {}
        data["Timeslot"] = timeslots
        data["RoomID"] = rooms
        data["Activity"] = activities
        data["Number of participants"] = N_students
        data["Room capacity"] = capacities
        

        return pd.DataFrame(data=data).sort_values(by="Timeslot")
    

    def calculate_malus_points(self):
        """
        Calculate the malus points for the schedule. The more malus points a 
        schedule has, the worse it is.
        """
        total_malus_points = 0
        for roomslot in self._roomslots:
           
            # There is 1 malus point for each student that is to many in a room
            malus_points = roomslot._N_participants - roomslot._capacity
            # If the capacity is sufficient, no malus points are awarded
            if malus_points <= 0:
                malus_points = 0

            # If an activity is at a timeslot from 17h-19h, 5 malus points are awarded
            if (roomslot._timeslot + 1) % 5 == 0 and roomslot._activity != 'Available':
                malus_points += 5

            total_malus_points += malus_points

        return total_malus_points


    def student_list(self):
        """
        Makes a list with all students as Student class instances
        """
        students = dict()

        for row in self._students_df.iterrows():
            name = row[1]["Achternaam"] + ', ' + row[1]["Voornaam"]
            student_number = row[1]["Stud.Nr."]
            courses = []
            for i in range (0, 5):                
                if isinstance((row[1][f"Vak{i + 1}"]),str):
                    course = row[1][f"Vak{i + 1}"]
                    courses.append(course)
                                        
            student = Student.Student(name, student_number, courses)        
            students[student_number] = student

        return students

        
    def save_schedule(self):
        self.show_schedule().to_csv("Rooster.csv")