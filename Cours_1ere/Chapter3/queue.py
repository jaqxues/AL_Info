class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, i):
        self.items.append(i)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        assert not self.is_empty(), "Queue is empty"
        return self.items.pop(0)

    def top(self):
        assert not self.is_empty(), "Queue is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return 'Queue; [' + ' '.join(map(str, self.items)) + ']'

if __name__ == '__main__':
    q = Queue()
    for i in range(1, 5):
        q.enqueue(i)
    print(q)
    print("Queue size:", q.size())
    while not q.is_empty():
        print(q.top())
        print(q.dequeue())
    print(q)
    print(q.dequeue())
