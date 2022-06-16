from code import helpers

class Student:
    """
    This class includes all student information
    """
    
    def __init__(self, data):
        self._student_name = data["Achternaam"] + ', ' + data["Voornaam"]
        self._studentnumber = data["Stud.Nr."]
        self._activities = set()
        self._courses = self.add_all_courses(data)
        self._malus_points = 0


    def add_all_courses(self, data):
        courses = []
        for i in range (0, 5):                
                if isinstance((data[f"Vak{i + 1}"]),str):
                    course = data[f"Vak{i + 1}"]
                    courses.append(course)
        return courses


    def malus_conflict(self):
        """
        Calculate the malus points for the student caused by conflicting activities.
        Each conflict results in 1 malus point.
        """
        timeslots = [activity._timeslot for activity in self._activities]
        malus_points: int = helpers.doubles_counter(timeslots)

        return malus_points


    def add_course(self, course):
        self._courses.add(course)


    def add_activity(self, activity):
        self._activities.add(activity)


    def __repr__(self):
        return f"{self._student_name}"
