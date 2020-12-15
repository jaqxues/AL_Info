from random import randrange, randint
from queue import Queue

from Cours_1ere.Chapter3.Ex3_13 import Desk, \
    NEW_ARRIVALS, SIMULATION_DAYS, DAY_DURATION, PATIENCE, TIME_NEEDED

n = int(input("Enter number of desks: "))

nb_served = nb_unserved = nb_gone = 0
waiting_time = 0
for _ in range(SIMULATION_DAYS):
    desks = [Desk() for _ in range(n)]
    q = Queue()
    for t in range(DAY_DURATION):
        if randrange(NEW_ARRIVALS) == 0:
            q.enqueue((t, t + randint(*PATIENCE)))
        for d in desks:
            if not d.is_busy():
                while not q.is_empty() and q.top()[1] < t:
                    q.dequeue()
                    nb_gone += 1
                if not q.is_empty():
                    waiting_time += t - q.dequeue()[0]
                    nb_served += 1
                    d.new_random_time(time_needed=TIME_NEEDED)
            d.tick()
    while not q.is_empty():
        if q.dequeue()[1] < DAY_DURATION:
            nb_gone += 1
        else:
            nb_unserved += 1

print("New client every", NEW_ARRIVALS, "seconds on average.")
print("Duration of Simulation:", DAY_DURATION, "seconds.")
print("Number of Simulations:", SIMULATION_DAYS)
print("Number of clients served:", nb_served)
print("Number of impatient clients:", nb_gone)
print("Number of unserved clients:", nb_unserved)
print(f"Average Waiting Time: {waiting_time / (nb_gone + nb_unserved + nb_served):.2f}")
