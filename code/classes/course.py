import math
from typing import Dict

import numpy as np

from . import activity as act


class Course:
    """
    This class contains the name of the course, all activities of the course, the attending 
    students and the maximum capactity of each activity.
    
    ...

    Attributes
    ----------
    self.course_name : str
        contains name of the course
    self.student_list : dict
        contains all students instances participating in the course {studentsnumber: student instance}
    self.activities : list
        contains all activity instances in the course
    self._N_activities : dict
        contains the number of each activity 
    self._capacity : dict
        contains the number of participants and the maximum of participants per practical or tutorial

    """
    def __init__(self, data) -> None:
        self.course_name = data["Vak"]
        self.student_list = {}        
        self.activities = []

        # Number of activities and max amount of students per activity type
        self._N_activities = {"Lectures": self.value(data["#Hoorcolleges"]), 
                             "Tutorials": self.value(data["#Werkcolleges"]), 
                             "Practicals": self.value(data["#Practica"])}

        self._capacity = {"Lectures": self.value(data["Verwacht"]), 
                         "Tutorials": self.value(data["Max. stud. Werkcollege"]), 
                         "Practicals": self.value(data["Max. stud. Practicum"])}
        
        self.student_list = {}
        
        self.activities = []
        
        self.activity_amount = self.activity_amount()
        

    
    def value(self, value):
        """
        If value is 'nan' then return 0, else return the value
        """
        if np.isnan(value) == True:
            return 0
        return value

    def sort_greedy(self):

        student_activity_dict = {}
        for student in self.student_list.values():
            student_activity_dict[student._studentnumber] = student.activity_amount

        dictionary_tuples = []
        for item in student_activity_dict.items():
            dictionary_tuples.append(item)
        


        dictionary_tuples.sort(key=lambda a: a[1])
        
            
        
        student_sorted = {}
        for studentnr,activity in dictionary_tuples:
            student_sorted[studentnr] = self.student_list[studentnr]

    
        self.student_list = student_sorted

    def make_activities(self, greedy=False): 
        """
        TODO Maak de activiteiten
        """
        
        if greedy:
            self.sort_greedy()
        
        for activity in self._N_activities:
            # Make an activity of every lecture
            if activity == "Lectures" and self._N_activities[activity] > 0 and len(self.student_list) > 0:
                # TODO: Group number
                for i in range(self._N_activities[activity]):
                    new_activity = act.Activity(activity, self.course_name, self.student_list, i) 
                    self.activities.append(new_activity)
                    self.activity_to_students(new_activity, self.student_list)

            # Make activities for all practicals and tutorials
            elif self._N_activities[activity] > 0 and len(self.student_list) > 0: 
                # Calculate the number of groups are needed for the amount of students
                number_of_groups = math.ceil( float(len(self.student_list) / self._capacity[activity]))

                # Number of students per groups
                group_size = math.ceil(len(self.student_list) / number_of_groups)

                # Equally devide the students over the number of groups
                divided_groups = self.divide_students(self.student_list, group_size)

                # Make the groups
                self.make_groups(divided_groups, self._N_activities[activity], activity, self.course_name)

    
    def activity_amount(self):

        activity_amount = 0 
        for activity in self._N_activities.values():
            activity_amount += activity
        return activity_amount



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
                self.activity_to_students(new_activity, group)
           
            group_id += 1

    def activity_to_students(self, activity, students: Dict) -> None:
        """
        Add the activity to the students in that group
        """
        for student in students.values():
            student.add_activity(activity)

    def divide_students(self, student_list: Dict, number_of_groups: int):
        """
        Distribute students in list of students over number of groups
        """
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