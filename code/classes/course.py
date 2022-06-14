import numpy as np
from . import activity
import math

class Course:

    def __init__(self, data) -> None:

        self.course_name = data["Vak"]

        # Number of activities and max amount of students per activity type
        self.N_activities = {"Lectures": data["#Hoorcolleges"], "Tutorials": data["#Werkcolleges"], "Practicals": data["#Practica"]}
        self.max_students = {"Lectures": data["Verwacht"], "Tutorials": data["Max. stud. Werkcollege"], "Practicals": data["Max. stud. Practicum"]}
        self.student_list = {}
        
        self.activities = []


    def make_activities(self): 
        for key in self.N_activities:
            if key == "Lectures":
                activity = Activity(key, self.course_name, self.student_list)
                self.activities.append(activity)
            else: 
                min_N_groups = (math.ceil(self.max_students["Lectures"] / self.max_students[key])) * self.N_activities[key]   

                split_student_list = np.array_split(self.student_list, min_N_groups)
                print(split_student_list)

                for student_list in split_student_list:
                    activity = Activity(key, self.course_name, student_list, group)
                    self.activities.append(activity)


    def __repr__(self):
        return f"{self.course_name}"
