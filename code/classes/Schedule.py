import math
import random
import copy
from typing import List, Set, Dict, Tuple, Optional
from tokenize import String

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from code import helpers
from code.classes.course import Course
from . import Roomslot, Student
from . import activity, course


class Schedule:
    """
    This class can be used to devide the courses over the 
    roomslots (room-timeslot pair)

    ...

    Attributes
    ----------
    self.courses_df : pandas dataframe 
        contains data about the courses
    self.rooms_df : pandas dataframe
        contains data about the rooms
    self._students_df : pandas dataframe
        contains data about the students
    self.courses : dict
        contains all course instances 
    self._students : dict
        contains all student instances
    self._activities : list
        contains all activity instances
    self._roomslots : list
        contains all roomslot instances
    """
    def __init__(self):
        self._courses_df = helpers.import_data("vakken")
        self._rooms_df = helpers.import_data("zalen")
        self._students_df = helpers.import_data("studenten_en_vakken")

        self.courses = self.course_dict()
        self._students = self.student_dict()
        self.add_students_to_courses()
        self._activities = self.activity_list()
        self._roomslots = self.roomslot_list()
        
    def roomslot_list(self):
        """
        Create roomslots by linking every room to a timeslot ()
        """
        roomslots = []

        room_ids = self.room_ids()
        room_capacities = self.room_capacities()
        largest_room_ID = self._rooms_df['Zaalnummber'].iloc[-1]
        largest_room_capacity = self._rooms_df['Max. capaciteit'].iloc[-1]
        
        # Make for every room in every timeslot a roomslot (there are 4*5=20 timeslots) 
        # Largest room has an extra timeslot (17-19u every day, so +5 timeslots)
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
        for course in self.courses.values():
            # Filter students that are signed in to "course"
            selected_students = self._students_df[(self._students_df["Vak1"] == f"{course.course_name}") | 
                                                  (self._students_df["Vak2"] == f"{course.course_name}") |
                                                  (self._students_df["Vak3"] == f"{course.course_name}") |
                                                  (self._students_df["Vak4"] == f"{course.course_name}") |
                                                  (self._students_df["Vak5"] == f"{course.course_name}") ]

            # Get student numbers
            students_Nrs = selected_students["Stud.Nr."].tolist()
            # Get student object
            students_object = [self._students.get(key) for key in students_Nrs]

            # Make dictionary of students participating in course
            students = {}
            for student_Nr, students_object in zip(students_Nrs, students_object):
                students[student_Nr] = students_object

            # Add students to course
            course.student_dict = students
            # Divide the students over the course activities
            course.make_activities(False)

    def room_ids(self) -> list:
        """
        Make list of all room ids
        """
        return self._rooms_df['Zaalnummber'].tolist()

    def room_capacities(self) -> list:
        """
        Make list of all room capacities
        """
        return self._rooms_df['Max. capaciteit'].tolist()

    def activity_list(self):
        """
        Make a list of all possible activities TODO
        """
        activities = []
        for course in self.courses.values():
            for activity in course.activities:
                activities.append(activity)

        return activities

    def make_schedule(self, algorithm):
        if algorithm == "random" or algorithm == "random_hillclimber":
            self.make_random_schedule()
        elif algorithm == "greedy_topdown" or algorithm == "greedy_topdown_hillclimber":
            self.make_greedy_schedule_topdown()
        elif algorithm == "greedy_bottomup" or algorithm == "greedy_bottomup_hillclimber":
            self.make_schedule_greedy_bottomup()
        
    def make_random_schedule(self) -> None:
        """
        Add all activities to a different timeslot
        """
        roomslots = set(self._roomslots)
        # Add all activities to schedule
        for activity in self._activities:

            # Get random roomslot 
            roomslot = random.choice(tuple(roomslots))

            # Place roomslot in activity
            activity.roomslot = roomslot 
            activity.timeslot = roomslot.timeslot
            roomslots.remove(roomslot)

            # Place activity in roomslot
            self.add_to_roomslot(activity, roomslot)
            

    def swap_roomslots(self, roomslot1, roomslot2):
        """
        Swap two activities in roomslots
        """
        # Swap activities in the roomslots
        save = roomslot1._activity_object
        roomslot1._activity_object = roomslot2._activity_object
        roomslot2._activity_object = save

        # Update the data in the roomslots based on their new activities
        roomslot1.update_data()
        roomslot2.update_data()

    def make_greedy_schedule_topdown(self) -> None:
        """
        Make a greedy schedule in which the activities with the highest 
        number of students are put into biggest rooms
        """
        self._roomslots.sort(key=lambda roomslots:roomslots._capacity, reverse=True)
        self._activities.sort(key=lambda activity:activity.total_students(), reverse=True)
        
        for activity,roomslot in zip(self._activities, self._roomslots):
            activity.roomslot = roomslot            
            self.add_to_roomslot(activity, roomslot)
            activity.timeslot = roomslot.timeslot
            
    def make_schedule_greedy_bottomup(self) -> None:
        """
        Puts activities with lowest number of students into smallest rooms
        """
        # Sort roomslots according to capacity and activities according to groupsize
        self._roomslots.sort(key=lambda roomslots:roomslots._capacity, reverse=False)
        self._activities.sort(key=lambda activities:activities.total_students(), reverse=False)

        # Link activities to roomslots and roomslots to activities
        for activity, roomslot in zip(self._activities, self._roomslots):
            activity.roomslot = roomslot 
            activity.timeslot = roomslot.timeslot
            self.add_to_roomslot(activity, roomslot)

    def two_random_roomslots(self):
        """
        Pick at random two nonidentical roomslots from all roomslots
        """
        roomslot1 = roomslot = random.choice(tuple(self._roomslots))
        roomslot2 = roomslot = random.choice(tuple(self._roomslots))

        while roomslot1 == roomslot2:
            roomslot2 = roomslot = random.choice(tuple(self._roomslots))
        
        return roomslot1, roomslot2

    def add_to_roomslot(self, activity, roomslot):
        """
        Assign activity to roomslot
        """
        roomslot.assign_activity(activity)    
        roomslot.N_participants = activity.total_students()

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

        # Get data from roomslot per roomslot
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

    def schedule_malus_points(self):
        """
        Calculate the malus points for the schedule. The more malus points a 
        schedule has, the worse it is.
        """
        malus_capacity = 0
        malus_evening = 0
        
        for roomslot in self._roomslots:
            # There is 1 malus point for each student that is to many in a room
            over_capacity = roomslot.N_participants - roomslot.capacity
            # If the capacity is sufficient, no malus points are awarded
            if over_capacity > 0:
                malus_capacity += over_capacity

            # If an activity is at a timeslot from 17h-19h, 5 malus points are awarded
            if (roomslot.timeslot + 1) % 5 == 0 and roomslot.course_name != 'Available':
                malus_evening += 5
        
        schedule_malus_points = malus_evening + malus_capacity

        return schedule_malus_points, malus_capacity, malus_evening

    def students_malus_points(self):
        """
        Calculate malus points per student
        """
        malus_conflict = 0
        malus_gaphour = 0

        for student in self._students.values():
            malus_conflict += student.malus_conflict()
            malus_gaphour += student.malus_gap_hours()

        student_malus_points = malus_conflict + malus_gaphour

        return student_malus_points, malus_conflict, malus_gaphour

    def total_malus_points(self):
        return (self.students_malus_points()[0] + self.schedule_malus_points()[0])

    def malus_analysis(self, name=""):
        """
        Analysis of the origin of the malus points
        """
        # Get malus points
        schedule_malus_points, malus_capacity, malus_evening = self.schedule_malus_points()
        student_malus_points, malus_conflict, malus_gaphour = self.students_malus_points()

        # Distribute data
        data = {'Capacity': malus_capacity, 'Evening': malus_evening, 'conflict': malus_conflict, 'gaphour': malus_gaphour}
        names = list(data.keys())
        values = list(data.values())

        # Make plot
        plt.bar(range(len(data)),values,tick_label=names)
        plt.savefig(f"images/malus_analysis{name}")
        plt.clf()

    def student_dict(self):
        """
        Makes a list with all students as Student class instances
        """
        students = {}

        for row in self._students_df.iterrows():            
            courses = []
            for i in range (0, 5):                
                    if isinstance((row[1][f"Vak{i + 1}"]),str):
                        courses.append(self.courses[(row[1][f"Vak{i + 1}"])])
            students[row[1]["Stud.Nr."]] = Student.Student(row[1], courses) 

        return students
        

    def save_schedule(self):
        self.show_schedule().to_csv("Rooster.csv")
