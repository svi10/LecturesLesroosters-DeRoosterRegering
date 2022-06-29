"""
We are going to make a schedule.
"""
import argparse

from code.classes import Schedule
from code.algorithms import random
from code.algorithms import greedy


def main(algorithm, N_repetitions):
    # Initialize schedule
    schedule = Schedule.Schedule()

    # Generate schedule
    schedule.make_schedule(algorithm)
    generated_schedule = schedule.show_schedule()
    schedule.save_schedule()

    # Calculate total malus points for this schedule
    total_malus_points = schedule.total_malus_points()

    print(f'\n The total number of malus points for this schedule is: {total_malus_points}. \n')
    print(generated_schedule.to_string(index=False), "\n")

    random_algorithm = random.Random(schedule)

    if algorithm == "greedy_topdown" or algorithm == "greedy_topdown_hillclimber":
        greedy_algorithm = greedy.Greedy(schedule, type="topdown")
    elif algorithm == "greedy_bottomup" or algorithm == "greedy_bottomup_hillclimber":
        greedy_algorithm = greedy.Greedy(schedule, type="bottomup")

    # -----------------------Random
    if algorithm == "random":
        # Random N time
        print(f"RANDOM {N_repetitions} X")
        print(f"The random schedule has: {random_algorithm.run_N_times(N=N_repetitions)} MP")
        random_algorithm.malus_analysis_random()
        print("DONE \n\n")

    # -----------------------Hillclimber random
    if algorithm == "random_hillclimber":
        # Run N time
        print(f"RANDOM HILLCLIMBER {N_repetitions} X")
        random_algorithm.N_hillclimber(N=N_repetitions, threshold=10)
        print("DONE \n \n")

    # -----------------------Greedy
    # Since Greedy is always sorted in the same manner, the outcome (MP) will always be the same.
    if algorithm == "greedy_topdown" or algorithm == "greedy_bottomup":
        print(f"GREEDY {N_repetitions} X")
        print(f"The greedy schedule has: {greedy_algorithm.run()} MP")
        print("DONE \n\n")

    # -----------------------Hillclimber Greedy
    if algorithm == "greedy_topdown_hillclimber" or algorithm == "greedy_bottomup_hillclimber":
        print(f"GREEDY HILLCLIMBER {N_repetitions} X")
        greedy_algorithm.N_hillclimber(N=N_repetitions, threshold=100)
        print("DONE \n\n")


if __name__ == "__main__":
    # Prompt user for algorithm and number of runs
    parser = argparse.ArgumentParser(description="Enter algorithm to be applied to schedule.")
    parser.add_argument("algorithm", type=str, choices=[
        'random',
        'greedy_topdown',
        'greedy_bottomup',
        'random_hillclimber',
        'greedy_bottomup_hillclimber',
        'greedy_topdown_hillclimber'
        ])
    parser.add_argument("N", type=int, help="Number of runs")
    args = parser.parse_args()

    # Run script using input from user
    main(args.algorithm, args.N)
