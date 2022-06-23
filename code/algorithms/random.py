from typing import List
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

from code.algorithms.hillclimber import Hillclimber_activities

class Random:

    def __init__(self, schedule) -> None:
        self.schedule = schedule


    def run(self) -> int:
        """
        Make random schedule and return the amount of malus points.
        """
        self.schedule.make_random_schedule()
        malus_points: int = self.schedule.total_malus_points()

        return malus_points
    

    def run_N_times(self, N: int) -> List:
        """
        Make N times a random schedule and keep track of the malus points
        """
        malus_points: List = []

        for i in range(N):
            malus_points.append(self.run())

        self.plot("empty", malus_points, title=f"Random Schedule ({N} keer)", savename="NRandom")

        return malus_points


    def hillclimber(self, threshold: int):
        """
        Apply hillclimber algorithm on random schedule and plot
        the results.
        """

        self.schedule.make_random_schedule()

        hillclimber = Hillclimber_activities(self.schedule)
        # Hillclimber
        mp_data, iterations_data = hillclimber.hillclimber(threshold=threshold)

        self.plot(x=iterations_data, y=mp_data, 
                  title=f"Random Hillclimber (Threshold = {threshold})", savename="Hillclimber_random")


    def plot(self, x: List, y: List, title: str, savename: str) -> None:
        """
        Make line plot of input data and save the result
        """
        # If no x list is given, generate one
        if x == "empty":
            x = list(range(1, len(y) + 1))

        # Initialize plot
        fig, ax = plt.subplots()

        # Customize plot
        ax.set_xlim(0, max(x))
        ax.set_ylim(0, max(y))
        plt.suptitle(f"{title}")
        ax.set_title(f"Gemiddeld: {round(sum(y) / len(y))} MP   Max: {max(y)} MP   Min: {min(y)} MP")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")

        ax.plot(x, y, color='blue')
        fig.savefig(f"images/{savename}")


    def N_hillclimber(self, N: int, threshold: int):
        """
        Run hillclimber N times on the same schedule
        """

        hillclimber = Hillclimber_activities(self.schedule)

        mp_data, iterations_data = hillclimber.run_N_times(N, threshold)

        self.plot(x=iterations_data, y=mp_data, title=f"Random Hillclimber ({N} keer)", savename="NHillclimber_random")

    def malus_analysis_random(self):
        self.schedule.make_random_schedule()
        self.schedule.malus_analysis("_Random")


        