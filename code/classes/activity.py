
class Activity:
    """
    This class contains the activitytype, the name of the activity and the list of students. 
    It can add, remove and show students.
    """

    def __init__(self, activitytype, name, student_list):
        self._type = activitytype
        self._name = name
        self._student_set = set(student_list.values())
        self._room = None
        self._timeslot = None

    def add_student(self, students):
        self._student_set.update(students)

    def remove_student(student):
        self._student_set.discard(student)

    def show_students(self):
        return self._student_set

    def get_name(self):
        return self._name

# if __name__ == "__main__":
#     activitytype = "tutorial"
#     course = "Algoritmen"
#     student_list = ["Student1", "Student2", "Student3"]
#     activity = Activity(activitytype, course, student_list)
#     students = activity.show_students()
#     print(students)

#     new_students = ["Student4"]
#     activity.add_student(new_students)
#     students = activity.show_students()
#     print(students)

#     print(activity)
#     print(activity.get_name())