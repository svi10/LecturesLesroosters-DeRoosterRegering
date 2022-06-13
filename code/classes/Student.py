from code import helpers

class Student:
    """
    This class includes all student information
    """
    

    def __init__(self):
        self._students_df = helpers.import_data("studentenvakken")
        
        self._name = []
        self._activities = []
        self._courses_df = []
        self._malus_points = []
