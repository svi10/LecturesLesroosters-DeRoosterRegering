"""
Wij gaan een rooster maken
"""

from code.classes import Schedule
from code.classes import Student

if __name__ == "__main__":
    schedule = Schedule.Schedule()
    # schedule.make_schedule()
    # df = schedule.show_schedule()
    # schedule.save_schedule()
    total_malus_points = schedule.calculate_malus_points()
    print(f'\n The total number of malus points for this schedule is: {total_malus_points}. \n')
    # print(df.to_string())
