class Roomslot:
    """
    A roomslot is a room-timeslot pair. A roomslot can only have one activity.
    """
    
    def __init__(self, roomID, timeslot, capacity):
        self._roomID = roomID
        self._capacity = capacity
        self._timeslot = timeslot
        self._course_name = 'Available'
        self._activity = 0
        self._activity_object = None
        self._N_participants = 0
        self._malus_points_roomslot = ''
    

    def assign_activity(self, activity):
        "Assign an activity to this roomslot"
        self._course_name = activity.get_course_name()
        self._activity_object = activity


    def get_data(self):
        
        data = {}

        data["Timeslot"] = self._timeslot
        data["Capacity"] = self._capacity
        data["Room ID"] = self._roomID

        if self._activity_object == None:
            data["Course name"] = "Empty"
            data["Number of participants"] = 0
            data["Type"] = "-"
        else:
            data["Course name"] = self._activity_object.get_course_name()
            data["Number of participants"] = self._activity_object.total_students()
            data["Type"] = self._activity_object._type

        return data

    def __repr__(self) -> str:
        return f"{self._timeslot}, {self._roomID}"