"""
Wij gaan een rooster maken
"""
import pandas as pd


def import_data():
    """
    Import the csv files of the courses and rooms as dataframes.
    
        Return courses, rooms
    """
    courses_df = pd.read_csv('vakken.csv', sep=';')
    rooms_df = pd.read_csv('zalen.csv', sep=';')
    
    return courses_df, rooms_df
    

class Schedule:
    """
    This class can be used to devide the courses over the 
    roomslots (room-timeslot pair)
    """
    
    def __init__(self):
        self._courses_df, self._rooms_df = import_data()
        self._activities = self.activity_list()
        
        self._roomslots = []
        room_ids = self.room_ids()
        
        # Make for every room in every timeslot a roomslot (there are 4*5=20 timeslots)
        for timeslot in range(20):
            for roomID in room_ids:
                roomslot = Roomslot(roomID, timeslot)
                self._roomslots.append(roomslot)

        
    def room_ids(self):
        return self._rooms_df['Zaalnummer'].tolist()
        
    
    def activity_list(self):
        """
        Make a list of all possible activities
        
        Example:
            
        ['Hoorcollege Advanced Heuristics', 
         'Practicum Advanced Heuristics', 
         'Hoorcollege Algoritmen en complexiteit', 
         'werkcollege Algoritmen en complexiteit', 
         'Practicum Algoritmen en complexiteit',
         ...
         ]
        """
        activities = []

        for row in self._courses_df.iterrows():
            # Name of the course
            vak = row[1]['Vakken']
            # Number of lectures, practicals and toturials
            N_lectures = row[1]["#Hoorcolleges"]
            N_practicals = row[1]["#Practica"]
            N_toturials = row[1]["#Werkcolleges"]
             
            for i in range(N_lectures):
                activities.append( ("Hoorcollege " + vak) )
            
            for i in range(N_toturials):
                activities.append("Werkcollege " + vak)
            
            for i in range(N_practicals):
                activities.append("Practicum " + vak)

        return activities
        
    
    def make_schedule(self):
        """
        Add all activities to a different timeslot
        """
        roomslot_number = 0
        for activity in self._activities:
            
            roomslot = self._roomslots[roomslot_number]
            roomslot.assign_activity(activity)
            
            roomslot_number += 1


    def show_schedule(self):
        """
        Show schedule in a dataframe
        """
        timeslots = []
        rooms = []
        activities = []
        
        for roomslot in self._roomslots:
            timeslots.append(roomslot._timeslot)
            rooms.append(roomslot._roomID)
            activities.append(roomslot._activity)
        
        data = {}
        data["Timeslot"] = timeslots
        data["RoomID"] = rooms
        data["Activity"] = activities
        
        return pd.DataFrame(data=data)
    
    
    def save_schedule(self):
        self.show_schedule().to_csv("Rooster.csv")
    

class Roomslot:
    """
    A roomslot is a room-timeslot pair. A roomslot can only have one activity.
    """
    
    def __init__(self, roomID, timeslot):
        self._roomID = roomID
        self._timeslot = timeslot
        self._activity = ''
    
    def assign_activity(self, activity):
        "Assign an activity to this roomslot"
        self._activity = activity
        
if __name__ == "__main__":
    schedule = Schedule()
    
    schedule.make_schedule()
    df = schedule.show_schedule()
    schedule.save_schedule()
    print(df)