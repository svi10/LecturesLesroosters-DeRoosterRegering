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
    print(generated_schedule.to_string(index=False))
    # print(df_student.to_string(index=False))


    #-----------------------Random
    if False: # TODO Dit moet ff mooier
        random_algorithm = random.Random(schedule)
        random_algorithm.run(iterations=10, animate=False)
        print("Random Algorithm DONE \n\n")


    #-----------------------Hillclimber random
    if False:
        # Run 1 Time
        print("RANDOM HILLCLIMBER")
        random_hillclimber = hillclimber.Hillclimber_activities(schedule, type="Random")
        mp_list, iterations_list = random_hillclimber.run(100)
        random_hillclimber.plot_results(mp_list, iterations_list, animate=True)
        print("DONE \n\n")
    
    if False:
        print("RANDOM HILLCLIMBER")
        # Run N times
        random_hillclimber = hillclimber.Hillclimber_activities(schedule, type="Random")
        random_hillclimber.run_batch(N=10, threshold=100)
        print("DONE")

    #-----------------------Greedy ()
    if False:
        schedule.make_greedy_schedule_topdown()
        print("Greedy Algorithm DONE \n\n")

        
    if False:
        schedule.make_greedy_schedule_bottomup()
        print("Greedy Algorithm DONE \n\n")
    

    #-----------------------Hillclimber greedy
    if False:
        # Run 1 Time
        print("GREEDY HILLCLIMBER")
        greedy_hillclimber = hillclimber.Hillclimber_activities(schedule, type="Greedy")
        mp_list, iterations_list = greedy_hillclimber.run(100)
        greedy_hillclimber.plot_results(mp_list, iterations_list, animate=False)
        print("DONE \n\n")
    
    if True:
        print("GREEDY HILLCLIMBER")
        # helpers.blockPrint()
        # Run N times
        greedy_hillclimber = hillclimber.Hillclimber_activities(schedule, type="Greedy")
        greedy_hillclimber.run_batch(N=50, threshold=100)
        # helpers.enablePrint()
        print("DONE")