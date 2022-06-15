from code import helpers

class Student:
    """
    This class includes all student information
    """
    
    def __init__(self, name, studentnumber, courses):
        self._name = name
        self._studentnumber = studentnumber
        self._activities = set()
        self._courses = courses
        self._malus_points = 0


    def add_course(self, course):
        self._courses.add(course)


    def add_activity(self, activity):
        self._activities.add(activity)


    def __repr__(self):
        return f"{self._name}"
