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
        TODO
        """

        for activity in self.N_activities:
            print(f"Activity in for loop: \n {activity}")
            # Make an activity of every lecture
            if activity == "Lectures":
                # TODO: Group number
                print(f"Student list for lectures:\n {self.student_list}")
                new_activity = act.Activity(activity, self.course_name, self.student_list, 0) 
                self.activities.append(new_activity)

            # Make activities for all practicals and tutorials
            else: 
                # Calculate the number of groups are needed for the amount of students
                print(f"Number of students: {len(self.student_list)}")
                print(f"Capacity: {self.capacity[activity]}")
                print(f"The division: \n {len(self.student_list) / self.capacity[activity]}")
                number_of_groups = math.ceil( float(len(self.student_list) / self.capacity[activity]) )
                # Equally devide the students over the number of groups
                devided_groups = np.array_split(self.student_list, number_of_groups)

                # Make the groups
                self.make_groups(devided_groups, self.N_activities[activity], activity, self.course_name)


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


    def __repr__(self):
        return f"{self.course_name}"
