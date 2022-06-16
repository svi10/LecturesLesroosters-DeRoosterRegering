
class Activity:
    """
    This class contains the activitytype, the name of the activity and the list of students. 
    It can add, remove and show students.
    """

    def __init__(self, activitytype, name, student_list, group_id):
        self._type = activitytype
        self._course_name = name
        self._student_set = set(student_list.values())
        self._timeslot = None
        self._group_id = group_id
       

    def add_student(self, students):
        """
        Adds a student to the list of students in a activity
        """
        self._student_set.update(students)

    def total_students(self):
        """
        Returns the total amount of students in the activity
        """
        return len(self._student_set)

    def remove_student(self, student):
        """
        Removes a single student from the list of students in a activity
        """
        self._student_set.discard(student)

    def show_students(self):
        """
        Returns a set including all the students
        """
        return self._student_set

    def get_course_name(self):
        """
        Gets the name of the course 
        """
        return self._course_name

    def __repr__(self) -> str:
        return f"{self._course_name}"