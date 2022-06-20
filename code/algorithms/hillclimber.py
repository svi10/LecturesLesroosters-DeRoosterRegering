

class Hillclimber_activities:
    """
    A hillclimber algorithm
    """

    def __init__(self, schedule) -> None:
        self.schedule = schedule
    
    def run(self, threshold: int, animated: bool=False) -> None:
        # Make a random schedule
        self.schedule.make_random_schedule()
        roomslots = self.schedule._roomslots
        # Calculate starting amount of malus points
        malus_current = self.schedule.total_malus_points()

        # Make changes until there is not have been made an approvement for "threshold" times
        unsuccessful = 0

        while unsuccessful < threshold:
            
            roomslot1, roomslot2 = self.schedule.two_random_roomslots()

            # Swap the activities 
            self.schedule.swap_roomslots(roomslot1, roomslot2)

            # Calculate malus points for new situation
            malus_points = self.schedule.total_malus_points()

            # Check if the schedule is impored. If so, keep the change. Else, change it back
            if malus_points < malus_current:
                # Keep the change
                malus_current = malus_points
                unsuccessful = 0
            else:
                # Undo the change
                self.schedule.swap_roomslots(roomslot1, roomslot2)
                unsuccessful += 1
            print(f"MP: {malus_current},    Unsuccessful: {unsuccessful}")
            