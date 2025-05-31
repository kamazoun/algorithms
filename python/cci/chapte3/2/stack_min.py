"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time
"""

class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise Exception("Stack is empty")
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def min(self):
        if not self.min_stack:
            raise Exception("Stack is empty")
        return self.min_stack[-1]

