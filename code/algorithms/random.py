import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import time

class Random:

    def __init__(self) -> None:
        schedule = schedule

    def run(self, iterations, animate=False):

        # Make animation
        fig, ax = plt.subplots()
        
        # Set plot limits
        ax.set_xlim(0, iterations)
        ax.set_ylim(0, 3000)

        data_malus = []
        ims = []

        # Track time
        start = time.time()

        # First frame
        self.schedule.make_random_schedule()
        data_malus.append(self.schedule.total_malus_points())

        im = ax.plot(data_malus, color='blue')
        ims.append([im])

        # Run model N times
        for run in range(iterations):
            self.schedule.make_random_schedule()
            data_malus.append(self.schedule.total_malus_points())
            
            im = ax.plot(data_malus, animated=True, color='blue')
            ims.append([im])

        # Measure runtime
        end_model = time.time()
        print(f"Runtime Model: {round(end_model-start, 2)}s")

        if animate == True:
            # Make animation
            ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                        repeat_delay=0)
        else:
            ax.plot(data_malus)
            ax.show()



