from main import main
import time

start = time.time()
n_runs = 10000
stop = 600

while time.time() - start < stop:
    main("random", n_runs)
    print("Done running random")

while time.time() - start < stop:
    main("random_hillclimber", n_runs)
    print("Done running random hillclimber")

while time.time() - start < stop:
    main("greedy_bottomup", n_runs)
    print("Done running greedy bottomup")

while time.time() - start < stop:
    main("greedy_bottomup_hillclimber", n_runs)
    print("Done running greedy bottomup hillclimber")
