import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import string
import sys

class Hillclimber_activities:
    """
    A hillclimber algorithm
    """

    def __init__(self, schedule, type) -> None:
        assert type == "Random" or type == "Greedy", f"Only algorithm choices: Random, Greedy. Not {type}"
        self.schedule = schedule
        self.type = type
        self.threshold = None


    def run(self, threshold: int, plot=True) -> None:
        """
        Run random or greedy hillclimber.
        """
        self.threshold = threshold
        # Make schedule (greedy or random)
        if self.type == "Greedy":
            self.schedule.make_greedy_schedule_topdown()
        if self.type == "Random":
            self.schedule.make_random_schedule()

        # Calculate starting amount of malus points
        malus_current = self.schedule.total_malus_points()

        # Save the progress
        mp_list = [malus_current]
        iterations_list = [0]

        # Make changes until there is not have been made an approvement for "threshold" times
        unsuccessful = 0
        iterations = 0

        # Climb the hill
        print(f"Running hillclimber until {threshold} unsuccessful changes")
        while unsuccessful < threshold:
            iterations += 1

            roomslot1, roomslot2 = self.schedule.two_random_roomslots()

            # Swap the activities 
            self.schedule.swap_roomslots(roomslot1, roomslot2)

            # Calculate malus points for new situation
            malus_points = self.schedule.total_malus_points()

            # Check if the schedule is impored. If so, keep the change. Else, change it back
            if malus_points < malus_current:
                # Keep the change
                malus_current = malus_points
                print(f"Attempts: {unsuccessful}", end='\r')
                unsuccessful = 0
                # Keep track of the improvements
                mp_list.append(malus_current)
                iterations_list.append(iterations)

            else:
                # Undo the change
                self.schedule.swap_roomslots(roomslot1, roomslot2)
                unsuccessful += 1
            
        if plot:
            self.plot_results(x=iterations_list, y=mp_list)

        return mp_list, iterations_list


    def plot_results(self, x, y):
        """
        Make plot of the given lists
        """

        fig, ax = plt.subplots()

        # Customize plot
        ax.set_title(f"Max: {max(y)} MP   Min: {min(y)} MP   Gemiddeld: {round(sum(y) / len(y))} MP")
        # ax.set_xlim(0, max(x))
        ax.set_ylim(0, max(y) + 10)
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")
        plt.suptitle(f"Hillclimber {self.type} (Threshold = {self.threshold})")

        ax.plot(x, y, color='blue')
        fig.savefig(f"Images/Hillclimber_plot_{self.type}")


    def run_batch(self, N, threshold):
        """
        Run random hillclimber N times and plot the results
        """
        print(f"Run {self.type} hillclimber {N} times")
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
            mp, iterations = self.run(threshold, plot=False)
            
            if i != 0:
                end = iterations_list[-1][-1]
                iterations = [(x + end) for x in iterations]

            # Save results
            mp_list.append(mp)
            iterations_list.append(iterations)

        # Make one list of the lists
        mp_list = sum(mp_list, [])
        iterations_list = sum(iterations_list, [])

        # Plot and save results
        fig, ax = plt.subplots()
        
        # Customize plot
        plt.suptitle(f"{self.type} Hillclimber {N} keer met threshold {threshold}")
        ax.set_title(f"Beste resultaat: {min(mp_list)}MP")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")
        ax.set_xlim(0, max(iterations_list))
        ax.set_ylim(0, max(mp_list))

        # Plot results
        ax.plot(iterations_list, mp_list)
        fig.savefig(f"images/NHillclimber_plot_{self.type}")



