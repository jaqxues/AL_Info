from random import randrange
from queue import Queue


class CarWash:
    def __init__(self, tw):
        self.time_wash = tw
        self.time_remaining = 0

    def busy(self):
        return self.time_remaining > 0

    def tick(self):
        if self.busy():
            self.time_remaining -= 1

    def start_wash(self):
        self.time_remaining = self.time_wash

    def __str__(self):
        return f'CarWash(total={self.time_wash}, remaining={self.time_remaining})'


TIME_NEEDED = 5 * 60
NEW_ARRIVALS = 240
DAY_LENGTH = 10 * 60 * 60
SIMULATION_DAYS = 10

nb_cars = nb_dirty = 0
waiting_time = 0
for _ in range(SIMULATION_DAYS):
    cw = CarWash(TIME_NEEDED)
    q = Queue()
    for s in range(DAY_LENGTH):
        if randrange(NEW_ARRIVALS) == 0:
            q.enqueue(s)
        if not q.is_empty() and not cw.busy():
            waiting_time += s - q.dequeue()
            nb_cars += 1
            cw.start_wash()
        cw.tick()
    nb_dirty += q.size()

print("Time required to wash a car:", TIME_NEEDED, "seconds.")
print("New arrivals every:", NEW_ARRIVALS, "seconds.")
print("Duration of Simulation:", DAY_LENGTH, "seconds")
print("Washed cars:", nb_cars)
print("Dirty cars:", nb_dirty)
print(f"Average time: {waiting_time/nb_cars:.2f} seconds.")