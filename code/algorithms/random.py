import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


class Random:

    def __init__(self, schedule) -> None:
        self.schedule = schedule

    def run(self, iterations, animate=False):
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
        ims = []

        # Track time
        start = time.time()

        # First frame
        self.schedule.make_random_schedule()
        data_malus.append(self.schedule.total_malus_points())

        im = ax.scatter(iters, data_malus, color='blue')
        ims.append([im])

        # Run model N times
        for run in range(iterations):
            self.schedule.make_random_schedule()
            data_malus.append(self.schedule.total_malus_points())
            iters.append(run+2)

            im = ax.scatter(iters, data_malus, animated=True, color='blue')
            ims.append([im])

        # Measure runtime
        end_model = time.time()
        print(f"Runtime Model: {round(end_model-start, 2)}s")

        # Calculate average amount of malus points of all iterations
        average = round(sum(data_malus) / len(data_malus))
        ax.set_ylim(0, max(data_malus))
        ax.set_title(f"Malus punten gemiddeld: {average}")

        if animate == True:
            # Make animation
            ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                        repeat_delay=0)
            print("SAVING>>>")
            ani.save("images/random_algorithm_animation.gif")
            end_animation = time.time()
            print(f"Runtime Animation: {end_animation - end_model}s")

        ax.clear()
         # Set plot limits
        ax.set_xlim(0, iterations)
        ax.set_ylim(0, max(data_malus))

        plt.suptitle("Random Algoritme")
        ax.set_title(f"Malus punten gemiddeld: {average}")
        ax.set_xlabel("Iteraties")
        ax.set_ylabel("Malus punten")
        ax.plot(iters, data_malus)
        fig.savefig("images/random_algorithm_plot")
        
        print(f"Average amount of malus points: {average}")



