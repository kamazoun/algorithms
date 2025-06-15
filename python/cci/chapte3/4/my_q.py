

class MyQueue:
    """
    Strategy (with author's hint and good night sleep:) ): We push whenever we want to enqueue, and when we want to dequeue, we `reverse` the first stack into the second stack. Then we pop from the second stack until it is empty.
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None