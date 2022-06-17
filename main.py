"""
Wij gaan een rooster maken
"""

from code.classes import Schedule
from code.classes import Student

if __name__ == "__main__":
    schedule = Schedule.Schedule()
    df = schedule.show_schedule()
    schedule.save_schedule()
    df_student = schedule.show_student(52311353)
    total_malus_points = schedule.schedule_malus_points()
    print(f'\n The total number of malus points for this schedule is: {total_malus_points}. \n')
    print(df.to_string(index=False))
    print()
    print(df_student.to_string(index=False))
