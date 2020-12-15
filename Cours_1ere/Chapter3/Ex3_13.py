from random import randrange, randint
from queue import Queue

NEW_ARRIVALS = 40
PATIENCE = 2 * 60, 10 * 60
TIME_NEEDED = 30, 5 * 60
DAY_DURATION = 8 * 60 * 60
SIMULATION_DAYS = 10


class Desk:
    def __init__(self):
        self.time_busy = 0

    def is_busy(self):
        return self.time_busy > 0

    def tick(self):
        if self.time_busy:
            self.time_busy -= 1

    def new_random_time(self, time_needed=TIME_NEEDED):
        self.time_busy = randint(*time_needed)


if __name__ == '__main__':
    nb_served = nb_gone = nb_unserved = 0
    waiting_time = 0
    for _ in range(SIMULATION_DAYS):
        d = Desk()
        q = Queue()
        for t in range(DAY_DURATION):
            if randrange(NEW_ARRIVALS) == 0:
                q.enqueue((t, t + randint(*PATIENCE)))
            if not d.is_busy():
                while not q.is_empty() and q.top()[1] < t:
                    # waiting_time += q.top()[1] - q.top()[0]
                    q.dequeue()
                    nb_gone += 1
                if not q.is_empty():
                    nb_served += 1
                    waiting_time += t - q.dequeue()[0]
                    d.new_random_time()
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
