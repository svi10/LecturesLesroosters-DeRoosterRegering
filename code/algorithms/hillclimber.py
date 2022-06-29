import time
import string
import sys
from typing import Type
import copy

import matplotlib.pyplot as plt
import matplotlib.animation as animation

from code.classes.Schedule import Schedule


class Hillclimber_activities:
    """
    A hillclimber algorithm that randomly swaps two roomslots in a schedule.
    
    ...

    Attributes
    ----------
    self.schedule : schedule instance
        contains a schedule instance

    """
    def __init__(self, schedule: Type[Schedule]) -> None:
        self.schedule: Type[Schedule] = schedule


    def hillclimber(self, threshold, plot=False):
        """
        Accepts a schedule and applies the hillclimber algorithm
        """
         # Calculate starting amount of malus points
        malus_current = self.schedule.total_malus_points()
        print(f"START MP: {malus_current}")

        # Save the progress
        mp_list = [malus_current]
        iterations_list = [0]

        # Make changes until there is not have been made an approvement for "threshold" times
        unsuccessful = 0
        iterations = 0

        save_swaps = []

        # Climb the hill
        print(f"Running hillclimber until {threshold} unsuccessful changes")
        while unsuccessful < threshold:
            iterations += 1

            roomslot1, roomslot2 = self.schedule.two_random_roomslots()

            # Swap the activities 
            self.schedule.swap_roomslots(roomslot1, roomslot2)

            # Calculate malus points for new situation
            malus_points = self.schedule.total_malus_points()

            # Check if the schedule is improved. If so, keep the change. Else, change it back
            if malus_points < malus_current:
                # Keep the change
                malus_current = malus_points
                print(f"Attempts: {unsuccessful}", end='\r')
                
                # Reset counter
                unsuccessful = 0

                # Keep track of the improvements
                mp_list.append(malus_current)
                iterations_list.append(iterations)

                # Remember the swaps done
                save_swaps.append([roomslot1, roomslot2])

            else:
                # Undo the change
                self.schedule.swap_roomslots(roomslot1, roomslot2)
                unsuccessful += 1

        self.schedule.malus_analysis("_Random hillclimber")
        self.undo_changes(save_swaps)

        return mp_list, iterations_list


    def undo_changes(self, save_swaps):

        for swap in reversed(save_swaps):
            self.schedule.swap_roomslots(swap[0], swap[1])


    def run_N_times(self, N, threshold):
        """
        Run random hillclimber N times and plot the results
        """
        print(f"Run hillclimber {N} times")
        
        # Lists to save the data
        mp_list = []
        iterations_list = []

        # Run hillclimber N times
        for i in range(N):
            print(f"Running: {i}", end='\r')
            # Nice print statements
            if i != 0:
                sys.stdout.write("\033[F") #back to previous line 
                sys.stdout.write("\033[K") #clear line 
            # Hillclimber
            mp, iterations = self.hillclimber(threshold=threshold)

            if i != 0:
                end = iterations_list[-1][-1]
                iterations = [(x + end) for x in iterations]

            # Save results
            mp_list.append(mp)
            iterations_list.append(iterations)

        # Make one list of the lists
        mp_list = sum(mp_list, [])
        iterations_list = sum(iterations_list, [])

        return mp_list, iterations_list