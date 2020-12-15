from queue import Queue
from random import randint, randrange


class Shopper:
    def __init__(self, check_out):
        self.n_bought = randint(1, 50)
        self.unweighted = randrange(20) == 0
        self.bad_card = randrange(50) == 0
        self.waiting_time = 0
        self.total_waiting_time = 0
        self.check_out = check_out

    def checkout_time(self):
        t = 5 * self.n_bought
        if self.unweighted:
            t += 55
        if self.bad_card:
            t += 165
        return t

    def nervous(self, check_out):
        self.waiting_time = 0
        self.check_out = check_out

    def tick(self):
        self.waiting_time += 1
        self.total_waiting_time += 1


NEW_ARRIVALS = 30
SIMULATION_DAYS = 5
DAY_DURATION = 8 * 60 * 60
NB_CHECKOUTS = 6

nb_customers = 0
for _ in range(SIMULATION_DAYS):
    n_queues = [Queue() for _ in range(NB_CHECKOUTS)]
    for t in range(DAY_DURATION):
        if randrange(NEW_ARRIVALS):
            min(reversed(n_queues), key=lambda q: q.size()).enqueue(t)
            for p in (q.top() for q in n_queues):
                if p - t % 60 == 0 and p != t:
                    pass
                # TODO

