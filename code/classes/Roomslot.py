from typing import Type
from code.classes.activity import Activity


class Roomslot:
    """
    A roomslot is a room-timeslot pair. A roomslot can only have one activity.

    ...

    Attributes
    ----------
    self._roomID : str
        contains name of the room
    self.capacity : int
        contains the number of students able to sit in the room
    self.timeslot : int
        contains the timeslot
    self.course_name : str
        contains the name of the course, when used (default is 'Available')
    self._activity_object : activity instance
        contains an activity instance (default is 'None')
    self.N_participants : int
        contains all students instances participating in the activity

    """
    def __init__(self, roomID: str, timeslot: int, capacity: int) -> None:
        self._roomID = roomID
        self.capacity = capacity
        self.timeslot = timeslot
        self.course_name = 'Available'
        self._activity_object = None
        self.N_participants = 0

    def assign_activity(self, activity: Type[Activity]) -> None:
        """
        Assign an activity to this roomslot
        """
        self.course_name = activity.get_course_name()
        self._activity_object = activity

    def get_data(self) -> dict:
        """
        Put data of Roomslot into a dictionary, data
        """
        data = {}

        data["Timeslot"] = self.timeslot
        data["Capacity"] = self.capacity
        data["Room ID"] = self._roomID

        # If roomslot not occupied by activity, set data to empty
        if self._activity_object is None:
            data["Course name"] = "Empty"
            data["Number of participants"] = self.N_participants
            data["Type"] = "-"
        else:
            data["Course name"] = self._activity_object.get_course_name() + "." \
                + str(self._activity_object.get_group_id())
            data["Number of participants"] = self._activity_object.total_students()
            data["Type"] = self._activity_object.get_activity_type()

        return data

    def update_data(self) -> None:
        """
        Link activity to roomslot and roomslot to activity
        """
        if self._activity_object is not None:
            self.course_name = self._activity_object.get_course_name()
            self.N_participants = len(self._activity_object._student_set)
            self._activity_object.roomslot = self
            self._activity_object.timeslot = self.timeslot

    def __repr__(self) -> str:
        return f"{self._roomID}"
