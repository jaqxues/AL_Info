from queue import Queue


def josephus(n, k):
    q = Queue()
    for i in range(1, n + 1):
        q.enqueue(i)
    while q.size() > 1:
        for _ in range(1, k):
            q.enqueue(q.dequeue())
        print(q.dequeue(), end=" ")
    print()
    return q.top()


n = int(input("Enter the number of people: "))
k = int(input("Enter k: "))
print("Last person to die:", josephus(n, k))
