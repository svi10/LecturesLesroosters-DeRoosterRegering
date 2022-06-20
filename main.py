"""
Wij gaan een rooster maken
"""

from code.classes import Schedule
from code.classes import Student


if __name__ == "__main__":
    # Initialize schedule
    schedule = Schedule.Schedule()

    # Generate schedule
    schedule.make_greedy_schedule_bottomup()
    generated_schedule = schedule.show_schedule()
    schedule.save_schedule()

    # Show indivdual schedule
    df_student = schedule.show_student(52311353)
    
    # Calculate total malus points for this schedule
    total_malus_points = schedule.total_malus_points()

    print(f'\n The total number of malus points for this schedule is: {total_malus_points}. \n')
    print(generated_schedule.to_string(index=False))
    # print(df_student.to_string(index=False))


    #-----------------------Random
    # schedule.make_random_schedule()


    #-----------------------Hillclimber random


    #-----------------------Greedy ()
    # schedule.make_greedy_schedule_bottomup()
    # schedule.make_greedy_schedule_topdown()
    

    #-----------------------Hillclimber greedy
