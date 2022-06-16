from tokenize import String
import pandas as pd
import math
import random
from typing import List, Set, Dict, Tuple, Optional

from soupsieve import select

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
        self._rooms_df = helpers.import_data("zalen")
        self._students_df = helpers.import_data("studenten_en_vakken")

        self._courses =  self.course_dict()
        # print(f"Courses: \n {self._courses}")
        self._students = self.student_dict()
        self.add_students_to_courses()
        # print(f"Students: \n {self._students}")
        self._activities = self.activity_set()
        # print(f"Activities: {self._activities}")
        self._roomslots = self.roomslot_list()

        
        self.sort_roomslots()
       

    def roomslot_list(self):
        """
        TODO
        """
        roomslots = []

        room_ids = self.room_ids()
        room_capacities = self.room_capacities()
        largest_room_ID = self._rooms_df['Zaalnummber'].iloc[-1]
        largest_room_capacity = self._rooms_df['Max. capaciteit'].iloc[-1]
        
        # Make for every room in every timeslot a roomslot (there are 4*5=20 timeslots). Largest room has an extra timeslot (17-19u every day, so +5 timeslots)
        for timeslot in range(0, 25):
            # Make roomslots for largest room, 17-19u every day
            if (timeslot + 1) % 5 == 0:
                roomslot = Roomslot.Roomslot(largest_room_ID, timeslot, largest_room_capacity)
                roomslots.append(roomslot)
            else:
                for roomID, capacity in zip(room_ids, room_capacities):
                    roomslot = Roomslot.Roomslot(roomID, timeslot, capacity)
                    roomslots.append(roomslot)

        return roomslots


    def course_dict(self):
        """
        Make a dictionary of course objects for each course in the Course DataFrame
        """
        courses = {}
        for row in self._courses_df.iterrows():
            courses[row[1]["Vak"]] = Course(row[1])
        
        return courses

    def add_students_to_courses(self):
        """
        Add to each course the students that signed in for that course
        """

        for course in self._courses.values():
            # Filter the students that are signed in to "course"
            selected_students = self._students_df[(self._students_df["Vak1"] == f"{course.course_name}") | 
                                                  (self._students_df["Vak2"] == f"{course.course_name}") |
                                                  (self._students_df["Vak3"] == f"{course.course_name}") |
                                                  (self._students_df["Vak4"] == f"{course.course_name}") |
                                                  (self._students_df["Vak5"] == f"{course.course_name}") ]

            # Get student numbers
            students_Nrs = selected_students["Stud.Nr."].tolist()
            # Get student object
            students_object = [self._students.get(key) for key in students_Nrs]

            # Make dictionary of students participating in the course
            students = {}
            for student_Nr, students_object in zip(students_Nrs, students_object):
                students[student_Nr] = students_object

            # Add students to course
            course.student_list = students
            # Divide the students over the course activities
            course.make_activities()


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


    def activity_set(self):
        """
        Make a list of all possible activities. TODO
        """
        activities = set()

        for course in self._courses.values():
            for activity in course.activities:
                activities.add(activity)

        return activities
        

    def make_schedule(self) -> None:
        """
        Add all activities to a different timeslot
        """
        roomslots = set(self._roomslots)
        # print(f"Activities: {self._activities}")
        # Add all activities to the schedule
        for activity in self._activities: 
            if len(roomslots) == 0:
                break
            # Get random roomslot 
            roomslot = random.choice(tuple(roomslots))
            roomslots.remove(roomslot)
            
            # print(f"Roomslot: {roomslot}")
            # print(f"Roomslots: \n {roomslots}")

            self.add_to_roomslot(activity, roomslot)


    def add_to_roomslot(self, activity, roomslot):
        roomslot.assign_activity(activity)
        roomslot._N_participants = activity.total_students()
        pass
        

    def show_schedule(self):
        """
        Show schedule in a dataframe
        """
        timeslot = []
        room = []
        course_name = []
        activity_type = []
        capacity = []
        N_students = []
    
        for roomslot in self._roomslots:
            data = roomslot.get_data()

            timeslot.append(data["Timeslot"])
            room.append(data["Room ID"])
            course_name.append(data["Course name"])
            activity_type.append(data["Type"])
            capacity.append(data["Capacity"])
            N_students.append(data["Number of participants"])

        data = {}
        data["Timeslot"] = timeslot
        data["RoomID"] = room
        data["Course name"] = course_name
        data["Type"] = activity_type
        data["Number of participants"] = N_students
        data["Room capacity"] = capacity
        

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


    def student_dict(self):
        """
        Makes a list with all students as Student class instances
        """
        students = dict()

        for row in self._students_df.iterrows():
            students[row[1]["Stud.Nr."]] = Student.Student(row[1])

        return students
    
    def save_schedule(self):
        self.show_schedule().to_csv("Rooster.csv")