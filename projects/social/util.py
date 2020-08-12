
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if len(self) > 0:
            return self.queue.pop(0)
        else:
            return None
    def __len__(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if len(self) > 0:
            return self.stack.pop()
        else:
            return None
    def __len__(self):
        return len(self.stack)

