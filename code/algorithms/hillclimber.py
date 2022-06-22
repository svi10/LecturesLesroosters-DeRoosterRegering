import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Hillclimber_activities:
    """
    A hillclimber algorithm
    """

    def __init__(self, schedule) -> None:
        self.schedule = schedule


    def run(self, threshold: int, plot=True, animate=False) -> None:
        # Make a random schedule
        self.schedule.make_greedy_schedule_topdown()
        # Calculate starting amount of malus points
        malus_current = self.schedule.total_malus_points()

        # Save the progress
        mp_list = []
        iterations_list = []

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
            self.plot_results(mp_list, iterations_list)

        return mp_list, iterations_list


    def run_batch(self, N, threshold):
        
        print(f"Run random hillclimber {N} times")
        # Lists to save the data
        mp_list = []
        iterations_list = []

        # Run hillclimber N times
        for i in range(N):
            print(f"Running: {i}", end='\r')
            # Hillclimber
            mp, iterations = self.run(threshold, False)
            
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
        plt.suptitle(f"Hillclimber {N} keer met threshold {threshold}")
        ax.set_title(f"Beste resultaat: {min(mp_list)}MP")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")
        ax.set_xlim(0, max(iterations_list))
        ax.set_ylim(0, max(mp_list))
        ax.plot(iterations_list, mp_list)
        fig.savefig("images/NHillclimber_plot")


    def plot_results(self, mp_list, iterations_list, animate: bool=False):

         # Make animation
        fig, ax = plt.subplots()
        
        # Set plot limits
        ax.set_xlim(0, max(iterations_list))
        ax.set_ylim(0, max(mp_list) + 10)
        plt.suptitle("Hillclimber (Random)")
        ax.set_title(f"Start: {mp_list[0]} MP   Eind: {mp_list[-1]} MP   \u0394MP = {mp_list[-1] - mp_list[0]} MP")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")
        ax.plot(iterations_list, mp_list, color = "blue")
        fig.savefig("images/Hillclimber_plot")
        ax.clear()

        if animate:

            # Set plot limits
            ax.set_xlim(0, max(iterations_list))
            ax.set_ylim(0, max(mp_list) + 10)
            plt.suptitle("Hillclimber")
            ax.set_xlabel("Iteraties")
            ax.set_ylabel("Malus punten")

            ims = []

            x = []
            y = []
            for iteration, mp in zip(iterations_list, mp_list):
                x.append(iteration)
                y.append(mp)

                im = ax.scatter(x, y, color='orange', animated=True)
                ims.append([im])
            
            # Make animation
            ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                        repeat_delay=100)
            print("SAVING>>>")
            ani.save("images/Hillclimber_animation.gif")
            

