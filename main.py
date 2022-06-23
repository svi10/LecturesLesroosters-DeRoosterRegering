"""
Wij gaan een rooster maken
"""

from code.classes import Schedule
from code.classes import Student

from code import helpers

from code.algorithms import random
from code.algorithms import hillclimber


if __name__ == "__main__":
    # Initialize schedule
    schedule = Schedule.Schedule()

    # Generate schedule
    schedule.make_greedy_schedule_topdown()
    generated_schedule = schedule.show_schedule()
    schedule.save_schedule()

    # Show indivdual schedule
    df_student = schedule.show_student(52311353)
    
    # Calculate total malus points for this schedule
    total_malus_points = schedule.total_malus_points()

    print(f'\n The total number of malus points for this schedule is: {total_malus_points}. \n')
    print(generated_schedule.to_string(index=False), "\n")
    # print(df_student.to_string(index=False))


    random_algorithm = random.Random(schedule)
    greedy_algorithm = greedy.Greedy(schedule, type="bottomup")

    #-----------------------Random
    if False: # TODO Dit moet ff mooier
        print("RANDOM 1X")
        print(f"The random schedule has: {random_algorithm.run()} MP")
        random_algorithm.malus_analysis_random()
        print("DONE \n\n")


    #-----------------------Hillclimber random
    if False:
        # Run 1 Time
        print("RANDOM HILLCLIMBER 1 KEER")
        random_algorithm.hillclimber(threshold=100)
        print("DONE \n \n")
    
    if False:
        print("RANDOM HILLCLIMBER")
        random_algorithm.N_hillclimber(N=10, threshold=10)
        print("DONE \n\n")

    #-----------------------Greedy ()
    if False:
        print("GREEDY 1X")
        print(f"The greedy schedule has: {greedy_algorithm.run()} MP")
        print("DONE \n\n")

    #-----------------------Hillclimber greedy
    if False:
        # Run 1 Time
        print("GREEDY HILLCLIMBER 1 KEER")
        greedy_algorithm.hillclimber(threshold=100)
        print("DONE \n \n")
    
    if True:
        print("GREEDY HILLCLIMBER N KEER")
        greedy_algorithm.N_hillclimber(N=10, threshold=10)
        print("DONE \n\n")
