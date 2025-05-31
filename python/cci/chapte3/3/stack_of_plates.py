"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
"""


class SetofStacks:
    def __init__(self, capacity):
        self.threshold = capacity
        self.stacks = [[]]

    def push(self, value):
        if len(self.stacks[-1]) >= self.threshold:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            raise Exception("All stacks are empty")
        value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return value
    
    def pop_at(self, index):
        # Initially missed this edge case.
        if index < 0 or index >= len(self.stacks):
            raise Exception("Index out of bounds")
        if not self.stacks[index]:
            raise Exception("Stack at index is empty")
        value = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return value
    

    class authors:
        pass