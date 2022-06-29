import time
from typing import List

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from code.algorithms.hillclimber import Hillclimber_activities

class Greedy:
    """
    A greedy algorithm

    ...

    Attributes
    ----------
    self.schedule : schedule instance
        contains the greedy schedule instance
    self.type : str
        contains what type of greedy should be applied

    """
    def __init__(self, schedule, type: str) -> None:
        assert type == "bottomup" or type == "topdown" or type == "students", f"Only choices: bottomup, topdown, students. Not: {type}"
        self.schedule = schedule
        self.type = type

    def run(self) -> int:
        """
        Make Greedy schedule and return the amount of malus points.
        """
        if type == "bottomup":
            self.schedule.make_schedule_greedy_bottomup()
        elif type == "topdown":
            self.schedule.make_greedy_schedule_topdown()
        else:
            self.schedule.make_random_schedule()

        malus_points: int = self.schedule.total_malus_points()

        return malus_points

    def hillclimber(self, threshold: int):
        """
        Apply hillclimber algorithm on Greedy schedule and plot
        the results.
        """
        if type == "bottomup":
            self.schedule.make_schedule_greedy_bottomup()
        elif type == "topdown":
            self.schedule.make_greedy_schedule_topdown()
        else:
            self.schedule.make_random_schedule() 

        # Make schedule and safe data
        hillclimber = Hillclimber_activities(self.schedule)
        mp_data, iterations_data = hillclimber.hillclimber(threshold=threshold)

        # Plot Greedy schedule data
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
        ax.set_xlabel("Iteraties", size=12)
        ax.set_ylabel("Malus punten", size=12)

        ax.plot(x, y, color='blue')
        fig.savefig(f"images/{savename}")


    def N_hillclimber(self, N: int, threshold: int):
        """
        Run hillclimber N times on the same schedule
        """
        # Make greedy schedule
        if type == "bottomup":
            self.schedule.make_schedule_greedy_bottomup()
        elif type == "topdown":
            self.schedule.make_greedy_schedule_topdown()
        else:
            self.schedule.make_random_schedule()

        # Perform hillclimber over created schedule
        hillclimber = Hillclimber_activities(self.schedule)

        # Safe data from hillclimber
        mp_data, iterations_data = hillclimber.run_N_times(N, threshold)

        # Plot hillclimber data
        self.plot(x=iterations_data, y=mp_data, title=f"Greedy Hillclimber ({N} keer)", savename="NHillclimber_Greedy")
        self.histogram(data=mp_data, title=f"Hillclimber Greedy ({N} keer)", savename=f"Greedy_Hillclimber_Nkeer")


    def histogram(self, data: List, title: str, savename: str) -> None:
        """
        Make a histogram of the input data.
        """
        average = round(sum(data) / len(data))
        standard_deviation = round(np.std(data))

        fig, ax = plt.subplots()
        
        plt.suptitle(f"{title}")
        ax.hist(data, bins=20)
        ax.axvline(average, color='orange')
        ax.set_xlabel("MP")
        ax.set_ylabel("N schedules")
        ax.set_title(f"Gemiddeld: {average} MP   \u03C3: {standard_deviation} MP   Max: {max(data)} MP   Min: {min(data)} MP")

        fig.savefig(f"images/{savename}")