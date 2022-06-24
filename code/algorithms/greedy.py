import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from typing import List


from code.algorithms.hillclimber import Hillclimber_activities

class Greedy:
    """
    A greedy algorithm
    """

    def __init__(self, schedule, type: str) -> None:
        assert type == "bottomup" or type == "topdown", f"Only choices: bottomup, topdown. Not: {type}"
        self.schedule = schedule
        self.type = type


    def run(self) -> int:
        """
        Make Greedy schedule and return the amount of malus points.
        """
        if type == "bottomup":
            self.schedule.make_greedy_schedule_bottomup()
        if type == "topdown":
            self.schedule.make_greedy_schedule_topdown()

        malus_points: int = self.schedule.total_malus_points()

        return malus_points


    def hillclimber(self, threshold: int):
        """
        Apply hillclimber algorithm on Greedy schedule and plot
        the results.
        """
        if type == "bottomup":
            self.schedule.make_greedy_schedule_bottomup()
        if type == "topdown":
            self.schedule.make_greedy_schedule_topdown()

        hillclimber = Hillclimber_activities(self.schedule)
        mp_data, iterations_data = hillclimber.hillclimber(threshold=threshold)

        self.plot(x=iterations_data, y=mp_data, 
                  title=f"Greedy Hillclimber (Threshold = {threshold})", savename="Hillclimber_Greedy")


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
        if type == "bottomup":
            self.schedule.make_greedy_schedule_bottomup()
        if type == "topdown":
            self.schedule.make_greedy_schedule_topdown()

        hillclimber = Hillclimber_activities(self.schedule)
        mp_data, iterations_data = hillclimber.run_N_times(N, threshold)

        self.plot(x=iterations_data, y=mp_data, title=f"Greedy Hillclimber ({N} keer)", savename="NHillclimber_Greedy")

