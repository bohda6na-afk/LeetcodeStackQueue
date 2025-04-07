from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.popleft()

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def __str__(self):
        return str(self.items)

class MyStack(object):

    def __init__(self):
        self.queue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.push(x)
        for _ in range(len(self.queue) - 1):
            self.queue.push(self.queue.pop())

    def pop(self):
        """
        :rtype: int
        """
        if not self.queue.is_empty():
            return self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.queue.is_empty():
            return self.queue.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0