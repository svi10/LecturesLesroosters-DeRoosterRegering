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


        self._malus_points += malus_points
        return malus_points

    def malus_gap_hours(self):
        """
        Calculate malus points for the student caused by gap hours in the schedule. 1 gap hours gives 
        1 malus point. 2 consecutive gap hours gives 3 malus points. 3 consecutive gap hours is not allowed.
        """
        timeslots = [activity._timeslot for activity in self._activities]
        # Distribute timeslots over the 5 days of the week
        week = []
        for i in range(5,26,5):
            day = set()
            remove = []

            for timeslot in timeslots:
                if timeslot < i:
                    day.add(timeslot)
                    remove.append(timeslot)
            
            for i in remove:
                timeslots.remove(i)

            week.append(sorted(day))

        # Calculate the number of gap hours and corresponding malus points
        malus_points = 0
        for day in week:
           
            for i in range(len(day)):
                if day[i] != day[-1]:
                    gap_hours = day[i+1] - day[i] - 1

                    # Reward malus points
                    if gap_hours == 1:
                        malus_points += 1
                    
                    if gap_hours == 2:
                        malus_points += 3
                    
                    if gap_hours == 3:
                        malus_points += 30
        self._malus_points += malus_points
        return malus_points


    def add_course(self, course):
        self._courses.add(course)


    def add_activity(self, activity):
        self._activities.add(activity)


    def __repr__(self):
        return f"{self._student_name}"
