import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class Random:

    def __init__(self, schedule) -> None:
        self.schedule = schedule

    def run(self, iterations):
        print(f"\nRun Random Algorithm {iterations} times...")
        # Make animation
        fig, ax = plt.subplots()
        
        # Set plot limits
        ax.set_xlim(0, iterations)
        ax.set_ylim(0, 3000)

        plt.suptitle("Random Algoritme")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")

        data_malus = []
        iters = [1]

        # Track time
        start = time.time()

        # First frame
        self.schedule.make_random_schedule()
        data_malus.append(self.schedule.total_malus_points())

        # Run model N times
        for run in range(iterations):
            self.schedule.make_random_schedule()
            data_malus.append(self.schedule.total_malus_points())
            iters.append(run+2)

        # Measure runtime
        end_model = time.time()
        print(f"Runtime Model: {round(end_model-start, 2)}s")

        # Calculate average amount of malus points of all iterations
        average = round(sum(data_malus) / len(data_malus))

        # Set plot limits
        ax.set_xlim(0, iterations)
        ax.set_ylim(0, max(data_malus))

        plt.suptitle(f"Random Algoritme ({iterations} keer)")
        ax.set_title(f"Gemiddeld: {average} MP   Max: {max(data_malus)} MP   Min: {min(data_malus)} MP")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")
        ax.plot(iters, data_malus)
        fig.savefig("images/random_algorithm_plot")
        
        print(f"Average amount of malus points: {average}")



