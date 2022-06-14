class Roomslot:
    """
    A roomslot is a room-timeslot pair. A roomslot can only have one activity.
    """
    
    def __init__(self, roomID, timeslot, capacity):
        self._roomID = roomID
        self._capacity = capacity
        self._timeslot = timeslot
        self._activity = 'Available'
        self._N_participants = 0
        self._malus_points_roomslot = ''
    

    def assign_activity(self, activity):
        "Assign an activity to this roomslot"
        self._activity = activity