
class Activity:
    """
    This class contains the activitytype, the name of the activity and the list of students. 
    It can add, remove and show students.
    """

    def __init__(self, activitytype, name, student_list, group_id):
        self._type = activitytype
        self._name = name
        self._student_set = set(student_list.values())
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
        return self._name
    
    def get_course_id(self):
        return self._group_id 

    def __repr__(self) -> str:
        return f"{self._name}, {self._group_id}"
