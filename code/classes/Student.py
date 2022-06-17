from code import helpers

class Student:
    """
    This class includes all student information
    """
    
    def __init__(self, data):
        self._student_name = data["Achternaam"] + ', ' + data["Voornaam"]
        self._studentnumber = data["Stud.Nr."]
        self._activities = set()
        self._courses = self.add_all_courses(data)
        self._malus_points = 0


    def add_all_courses(self, data):
        courses = []
        for i in range (0, 5):                
                if isinstance((data[f"Vak{i + 1}"]),str):
                    course = data[f"Vak{i + 1}"]
                    courses.append(course)
        return courses


    def malus_conflict(self):
        """
        Calculate the malus points for the student caused by conflicting activities.
        Each conflict results in 1 malus point.
        """
        timeslots = [activity._timeslot for activity in self._activities]
        malus_points: int = helpers.doubles_counter(timeslots)

        return malus_points


    def malus_gap_hours(self):
        """
        Calculate the malus points for each time a student has one or two gap hours. 
        One gap hour results in 1 malus point. Two gap hours result in three malus points.
        """
        malus_points_gaps = 0
        timeslots = [activity._timeslot for activity in self._activities]
        timeslots.sort()
        print(timeslots)
        week = []
        
        # Create list per days, where i is start of next day
        for i in range(5, 30, 5):
            day = []

            # Separate timeslots according to day
            for timeslot in timeslots:
                if timeslot < i:
                    day.append(timeslot)
                    timeslots.remove(timeslot)

            # Add day to week
            week.append(day)

            if len(day) > 1:
                for timeslot in day:
                    if day[+1] < i and day[+1] - timeslot == 2:
                        malus_points_gaps += 3
                    elif day[+1] < i and day[+1] - timeslot == 1:
                        malus_points_gaps += 1

        print(week)
            
        # print(f"Student: {self._student_name}")
        # print(f"Timeslots: {timeslots}")
        print(f"Malus points: {malus_points_gaps}")
        return malus_points_gaps
        
        
    def add_course(self, course):
        self._courses.add(course)


    def add_activity(self, activity):
        self._activities.add(activity)


    def __repr__(self):
        return f"{self._student_name}"
