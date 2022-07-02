from code.classes.Schedule import Schedule
from code.algorithms.random import Random
from code.algorithms.greedy import Greedy

import time
import numpy as np
import matplotlib.pyplot as plt

def experiment(runtime: int):
    """
    Run greedy hillclimber for different thresholds for a given
    amount of time (seconds).
    """

    schedule = Schedule("bottomup")
    greedy_algorithm = Greedy(schedule, "bottomup")
    

    # Set start time
    start = time.time()

    # Set start threshold
    threshold = 10

    threshold_data = []
    best_results_mp = []

    while time.time() - start < runtime:
        
        # Run the algorithm
        mp_data = greedy_algorithm.N_hillclimber(N=10, threshold=threshold)

        # Save data
        threshold_data.append(threshold)
        best_results_mp.append(min(mp_data))

        # Update threshold
        threshold += 100
    
    # Save data
    np.savetxt("FinalData/experiment_mp.csv", np.asarray(best_results_mp))
    np.savetxt("FinalData/experiment_threshold.csv", np.asarray(threshold_data))

    # Plot results
    plt.clf()
    plt.plot(threshold_data, best_results_mp, color="blue")
    plt.xlabel("Threshold")
    plt.ylabel("Malus punten")
    plt.xlim(0, max(threshold_data) + 50)
    plt.ylim(0, max(mp_data) + 50)
    plt.title("Experiment")
    plt.savefig("Images/experiment.png")

    return threshold_data, best_results_mp


if __name__ == "__main__":

    threshold_data, best_results_mp = experiment(900)
