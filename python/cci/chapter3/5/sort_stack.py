"""

"""

class SortStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        temp_stack = []
        while self.stack and self.stack[-1] > item:
            temp_stack.append(self.stack.pop())
        self.stack.append(item)
        while temp_stack:
            self.stack.append(temp_stack.pop())

