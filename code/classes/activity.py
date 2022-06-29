class Activity:
    """
    This class contains the activitytype, the name of the activity and the list of students.
    It can add, remove and show students.

    ...

    Attributes
    ----------
    self._type : str
        contains the type of activity
    self.course_name : str
        contains name of the course
    self._student_set : set
        contains all students instances participating in the course
    self._group_id : str
        contains the id of the room the activity is in
    self.timeslot : int
        contains the timeslot of the activity (default is 'None')
    self.roomslot : int
        contains the roomslot of the activity (default is 'none')

    """
    def __init__(self, activitytype: str, name: str, student_dict: dict, group_id: int):
        self._type = activitytype
        self.course_name = name
        self._student_set = set(student_dict.values())
        self._group_id = group_id
        self.timeslot = None
        self.roomslot = None

    def total_students(self) -> int:
        """
        Returns the total amount of students in the activity
        """
        return len(self._student_set)

    def get_course_name(self) -> str:
        return self.course_name

    def get_group_id(self) -> int:
        return self._group_id

    def get_activity_type(self) -> str:
        return self._type

    def __repr__(self) -> str:
        return f"{self._course_name}"
