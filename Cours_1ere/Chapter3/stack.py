class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, i):
        self.items.append(i)

    def pop(self):
        assert not self.is_empty(), "Stack is empty"
        return self.items.pop()

    def top(self):
        assert not self.is_empty(), "Stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return 'Stack (from top to bottom): [' + " ".join(map(str, reversed(self.items))) + ']'


if __name__ == '__main__':
    stack = Stack()
    print("Pushing")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Stack size:", stack.size())
    print(stack)
    while not stack.is_empty():
        print(stack.top(), end=" ")
        stack.pop()
    print()
    print('Stack size:', stack.size())
