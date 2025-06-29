"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
Hints:# 15, #32, #43
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

    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        raise IndexError("peek from empty stack")   

    def is_empty(self):
        return len(self.stack) == 0

