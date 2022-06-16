from typing import Dict
import numpy as np
from . import activity as act
import math


class Course:

    def __init__(self, data) -> None:

        self.course_name = data["Vak"]

        # Number of activities and max amount of students per activity type
        self.N_activities = {"Lectures": self.value(data["#Hoorcolleges"]), 
                             "Tutorials": self.value(data["#Werkcolleges"]), 
                             "Practicals": self.value(data["#Practica"])}

        self.capacity = {"Lectures": self.value(data["Verwacht"]), 
                         "Tutorials": self.value(data["Max. stud. Werkcollege"]), 
                         "Practicals": self.value(data["Max. stud. Practicum"])}
        
        self.student_list = {}
        
        self.activities = []

    
    def value(self, value):
        """
        If value is 'nan' then return 0, else return the value
        """
        if np.isnan(value) == True:
            return 0
        return value


    def make_activities(self): 
        """
        TODO Maak de activiteiten
        """

        for activity in self.N_activities:
            # Make an activity of every lecture
            if activity == "Lectures" and self.N_activities[activity] > 0 and len(self.student_list) > 0:
                # TODO: Group number
                new_activity = act.Activity(activity, self.course_name, self.student_list, 0) 
                self.activities.append(new_activity)

            # Make activities for all practicals and tutorials
            elif self.N_activities[activity] > 0 and len(self.student_list) > 0: 
                # Calculate the number of groups are needed for the amount of students
                number_of_groups = math.ceil( float(len(self.student_list) / self.capacity[activity]))

                # Number of students per groups
                group_size = math.ceil(len(self.student_list) / number_of_groups)

                # Equally devide the students over the number of groups
                divided_groups = self.divide_students(self.student_list, group_size)

                # Make the groups
                self.make_groups(divided_groups, self.N_activities[activity], activity, self.course_name)
                # Make activity
                new_activity = act.Activity(activity, self.course_name, self.student_list, 0) 
                self.activities.append(new_activity)


    def make_groups(self, groups, N_activities, activity_type, course_name):
        """
        The student groups are assigned to individual activities. If there are for example 3 tutorials,
        then each group is assigned to 3 tutorials.
        """

        group_id = 1
        # Assign groups to activity
        for group in groups:

            # If there are for example 3 tutorials, then 3 tutorials are made for that group
            for i in range(N_activities):
                new_activity = act.Activity(activity_type, course_name, group, group_id)
                self.activities.append(new_activity)
           
            group_id += 1

    def divide_students(self, student_list: Dict, number_of_groups: int):
        
        def split_dict(d, n):
            keys = list(d.keys())
            for i in range(0, len(keys), n):
                yield {k: d[k] for k in keys[i: i + n]}
        
        groups = []
        for item in split_dict(student_list, number_of_groups):
            groups.append(item)

        return groups

    def __repr__(self):
        return f"{self.course_name}"
