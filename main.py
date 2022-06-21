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
        random_hillclimber = hillclimber.Hillclimber_activities(schedule)
        random_hillclimber.run(100)
        random_hillclimber.plot_results(animate=True)
        print("Hillclimber DONE \n\n")
    
    if True:
        print("Run hillclimber N times")
        # helpers.blockPrint()
        # Run N times
        random_hillclimber = hillclimber.Hillclimber_activities(schedule)
        random_hillclimber.run_batch(N=10, threshold=100)
        # helpers.enablePrint()




    #-----------------------Greedy ()
    if False:
        schedule.make_greedy_schedule_bottomup()
        schedule.make_greedy_schedule_topdown()
    

    #-----------------------Hillclimber greedy
