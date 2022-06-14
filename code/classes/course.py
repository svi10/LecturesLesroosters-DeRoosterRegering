
class Course:

    def __init__(self, data) -> None:

        self.course_name = data["Vak"]

        # Number of activities and max amount of students per activity type
        self.activities = {"Lectures": data["#Hoorcolleges"], "Tutorials": data["#Werkcolleges"], "Practicals": data["#Practica"]}
        self.max_students = {"Lectures": data["Verwacht"], "Tutorials": data["Max. stud. Werkcollege"], "Practicals": data["Max. stud. Practicum"]}

        self.student_list = dict()


    def make_activities(self):
        pass


    def __repr__(self):
        return f"{self.course_name}"