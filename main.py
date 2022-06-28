"""
We are going to make a schedule.
"""
from sys import argv
import argparse

from code import helpers
from code.classes import Schedule
from code.classes import Student
from code.algorithms import random
from code.algorithms import greedy
from code.algorithms import hillclimber


def main(algorithm, N_repetitions):    
    # Initialize schedule
    schedule = Schedule.Schedule()

    # Generate schedule
    schedule.make_schedule(algorithm)
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
    
    if algorithm == "greedy_topdown" or algorithm == "greedy_topdown_hillclimber":
        greedy_algorithm = greedy.Greedy(schedule, type="topdown")
    elif algorithm == "greedy_bottomup" or algorithm == "greedy_bottomup_hillclimber":
        greedy_algorithm = greedy.Greedy(schedule, type="bottomup")

    #-----------------------Random
    if algorithm == "random":
        # Random N keer
        print(f"RANDOM {N_repetitions} KEER")
        print(f"The random schedule has: {random_algorithm.run_N_times(N=N_repetitions)} MP")
        random_algorithm.malus_analysis_random()
        print("DONE \n\n")

    #-----------------------Hillclimber random
    if algorithm == "random_hillclimber":
        # Run 1 Time
        print(f"RANDOM HILLCLIMBER {N_repetitions} KEER")
        random_algorithm.N_hillclimber(N=N_repetitions, threshold=10)
        print("DONE \n \n")

    #-----------------------Greedy
    if algorithm == "greedy_topdown" or algorithm == "greedy_bottomup":
        print("GREEDY 1X")
        print(f"The greedy schedule has: {greedy_algorithm.run()} MP")
        print("DONE \n\n")

    #-----------------------Hillclimber Greedy
    if algorithm == "greedy_topdown_hillclimber" or algorithm == "greedy_bottomup_hillclimber":
        print(f"GREEDY HILLCLIMBER {N_repetitions} KEER")
        greedy_algorithm.N_hillclimber(N=N_repetitions, threshold=100)
        print("DONE \n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter algorithm to be applied to schedule.")
    parser.add_argument("algorithm", type=str, choices=['random', 'greedy_topdown', 'greedy_bottomup', 
        'random_hillclimber', 'greedy_bottomup_hillclimber', 'greedy_topdown_hillclimber'])
    parser.add_argument("N", type=int, help="Number of Hillclimbers")
    args = parser.parse_args()

    main(args.algorithm, args.N)