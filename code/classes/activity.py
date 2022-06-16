
class Activity:
    """
    This class contains the activitytype, the name of the activity and the list of students. 
    It can add, remove and show students.
    """

    def __init__(self, activitytype, name, student_list, group_id):
        self._type = activitytype
        self._course_name = name
        self._student_set = set(student_list.values())
        self._room = None
        self._timeslot = None
        self._group_id = group_id
       

    def add_student(self, students):
        self._student_set.update(students)

    def total_students(self):
        return len(self._student_set)

    def remove_student(self, student):
        self._student_set.discard(student)

    def show_students(self):
        return self._student_set

    def get_course_name(self):
        return self._course_name

    def __repr__(self) -> str:
        return f"{self._course_name}"


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