import pandas as pd
from typing import List, Set, Dict, Tuple, Optional
from . import Roomslot
from code import helpers


class Schedule:
    """
    This class can be used to devide the courses over the 
    roomslots (room-timeslot pair)
    """

    def __init__(self):
        self._courses_df, self._rooms_df = helpers.import_data()
        self._activities = self.activity_list()

        self._roomslots = []
        room_ids = self.room_ids()
        room_capacities = self.room_capacities()

        # Make for every room in every timeslot a roomslot (there are 4*5=20 timeslots)
        for timeslot in range(0, 20):
            for roomID, capacity in zip(room_ids, room_capacities):
                roomslot = Roomslot.Roomslot(roomID, timeslot, capacity)
                self._roomslots.append(roomslot)
       
        self.sort_roomslots()



    def sort_roomslots(self):
        """
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
        return self._rooms_df['Zaalnummer'].tolist()


    def room_capacities(self) -> list:
        """Make list of all room capacities"""
        return self._rooms_df['Capaciteit'].tolist()


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
            vak = row[1]['Vakken']
            # Number of lectures, practicals and tutorials
            N_lectures = row[1]["#Hoorcolleges"]
            N_practicals = row[1]["#Practica"]
            N_tutorials = row[1]["#Werkcolleges"]
             
            for i in range(N_lectures):
                activity = {}
                activity['Activity'] = "Hoorcollege " + vak
                activity['E(studenten)'] = row[1]['E(studenten)']
                activities.append(activity)
            
            for i in range(N_tutorials):
                activity = {}
                activity['Activity'] = "Werkcollege " + vak
                activity['E(studenten)'] = row[1]['E(studenten)']
                activities.append(activity)
            
            for i in range(N_practicals):
                activity = {}
                activity['Activity'] = "Practicum " + vak
                activity['E(studenten)'] = row[1]['E(studenten)']
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
        N_students = activity['E(studenten)']
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
        # data["Malus points"] = malus_points
    
        return pd.DataFrame(data=data)
    

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


    def save_schedule(self):
        self.show_schedule().to_csv("Rooster.csv")