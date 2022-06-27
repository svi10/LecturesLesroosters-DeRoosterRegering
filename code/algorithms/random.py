import time
from typing import List

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from code.algorithms.hillclimber import Hillclimber_activities


class Random:
    """
    Class that creates an algortihm that generates a random schedule
    
    ...

    Attribute
    ----------
    self.schedule : schedule instance
        contains a random schedule instance
    
    """
    def __init__(self, schedule) -> None:
        self.schedule = schedule

    def run(self) -> int:
        """
        Make random schedule and return amount of malus points.
        """
        self.schedule.make_random_schedule()
        malus_points: int = self.schedule.total_malus_points()

        return malus_points

    def run_N_times(self, N: int) -> List:
        """
        Make N times a random schedule and keep track of malus points
        """
        malus_points: List = []

        for i in range(N):
            malus_points.append(self.run())

        self.histogram(malus_points, title=f"Random ({N} keer)")

        return malus_points

    def hillclimber(self, threshold: int):
        """
        Apply hillclimber algorithm on random schedule and plot results.
        """
        self.schedule.make_random_schedule()

        hillclimber = Hillclimber_activities(self.schedule)
        # Assign hillclimber information to data
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
        plt.clf()


    def histogram(self, data: List, title: str) -> None:
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

        fig.savefig("Images/Random_Histogram_Nkeer")
        


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
