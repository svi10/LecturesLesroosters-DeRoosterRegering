from code import helpers

class Student:
    """
    This class includes all student information
    """
    

    def __init__(self, name, studentnumber, courses):
        self._name = name
        self._studentnumber = studentnumber
        self._activities = None
        self._courses = courses
        self._malus_points = 0

    def __repr__(self):
        return f"{self._name}"
