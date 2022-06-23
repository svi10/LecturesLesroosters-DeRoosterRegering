import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class Greedy:

    def __init__(self, schedule) -> None:
        self.schedule = schedule


    def run(self, iterations):
        """
        Run the greedy algorithm and plot the results
        """
        print(f"\nRun Greedy Algorithm {iterations} times...")
        # Make plot
        fig, ax = plt.subplots()

        data_malus = []
        iters = [1]

        # Track time
        start = time.time()

        # First frame
        self.schedule.make_greedy_schedule_topdown()
        data_malus.append(self.schedule.total_malus_points())

        # Run model N times
        for run in range(iterations):
            self.schedule.make_greedy_schedule_topdown()
            data_malus.append(self.schedule.total_malus_points())
            iters.append(run+2)

        # Measure runtime
        end_model = time.time()
        print(f"Runtime Model: {round(end_model-start, 2)}s")

        # Calculate average amount of malus points of all iterations
        average = round(sum(data_malus) / len(data_malus))

        # Customize plot
        ax.set_xlim(0, iterations)
        ax.set_ylim(0, max(data_malus))
        plt.suptitle("Greedy Algoritme")
        ax.set_title(f"Malus punten gemiddeld: {average}")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")

        # Plot results
        ax.plot(iters, data_malus)
        fig.savefig("images/greedy_algorithm_plot")

        print(f"Average amount of malus points: {average}")
