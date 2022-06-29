class Activity:
    """
    This class contains the activitytype, the name of the activity and the list of students.
    It can add, remove and show students.

    ...

    Attributes
    ----------
    self._type : str
        contains the type of activity
    self._course_name : str
        contains name of the course
    self._student_list : set
        contains all students instances participating in the course
    self._group_id : str
        contains the id of the room the activity is in
    self.timeslot : int
        contains the timeslot of the activity (default is 'None')
    self.roomslot : int
        contains the roomslot of the activity (default is 'none')

    """
    def __init__(self, activitytype, name, student_list, group_id):
        self._type = activitytype
        self.course_name = name
        self.student_list = set(student_list.values())
        self._group_id = group_id
        self.timeslot = None
        self.roomslot = None

    def add_student(self, students):
        """
        Adds a student to the list of students in a activity
        """
        self._student_set.update(students)

    def total_students(self):
        """
        Returns the total amount of students in the activity
        """
        return len(self.student_list)

    def get_course_name(self):
        return self.course_name

    def get_group_id(self):
        return self._group_id

    def get_activity_type(self):
        return self._type

    def __repr__(self) -> str:
        return f"{self._course_name}"
