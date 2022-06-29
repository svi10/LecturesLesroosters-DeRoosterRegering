from code import helpers
from typing import Type

from code.classes.course import Course
from code.classes.activity import Activity


class Student:
    """
    This class includes all student information

    ...

    Attributes
    ----------
    self._student_name : str
        contains name of the student
    self.studentnumber : int
        contains the studentsnumber of the student
    self._activities : set
        contains all activity instances that the student participates in
    self._courses : list
        contains all courses that the student participates in
    self._malus_points : int
        contains the number of maluspoints that the student has
    self._activity_amount: int
        contains the number of activities the student partakes in

    """
    def __init__(self, data, course_objects: Type[Course]):
        self._student_name = data["Achternaam"] + ', ' + data["Voornaam"]
        self.studentnumber = data["Stud.Nr."]
        self._activities = set()
        self._courses = course_objects
        self._malus_points = 0
        self._activity_amount = self.activity_amount()

    def activity_amount(self) -> None:
        activity_amount = 0
        courses = self._courses
        for course in courses:
            activity_amount += course.activity_amount
        self._activity_amount = activity_amount

    def malus_conflict(self) -> int:
        """
        Calculate the malus points for the student caused by conflicting activities.
        Each conflict results in 1 malus point.
        """
        timeslots = [activity.timeslot for activity in self._activities]
        malus_points: int = helpers.doubles_counter(timeslots)

        self._malus_points += malus_points

        return malus_points

    def malus_gap_hours(self) -> int:
        """
        Calculate malus points for the student caused by gap hours in the schedule. 1 gap hours gives
        1 malus point. 2 consecutive gap hours gives 3 malus points. 3 consecutive gap hours is not allowed.
        """
        timeslots = [activity.timeslot for activity in self._activities]
        # Distribute timeslots over the 5 days of the week
        week = []
        for i in range(5, 26, 5):
            day = set()
            remove = []

            for timeslot in timeslots:
                if timeslot is not None and timeslot < i:
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
                    gap_hours = day[i + 1] - day[i] - 1

                    # Reward malus points
                    if gap_hours == 1:
                        malus_points += 1

                    if gap_hours == 2:
                        malus_points += 3

                    if gap_hours == 3:
                        malus_points += 30
        self._malus_points += malus_points

        return malus_points

    def add_activity(self, activity: Type[Activity]) -> None:
        """
        Add activity object to student
        """
        self._activities.add(activity)

    def __repr__(self) -> str:
        return f"{self._student_name}"
