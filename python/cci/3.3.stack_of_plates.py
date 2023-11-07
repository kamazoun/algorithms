R'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''
import collections

class StackNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    # def __repr__(s)


class Stack():
    def __init__(self, top): # I force the initialization of top when creating a stack
        self.top = top
        self.items = 1

    # def __repr__(s)

    def push(self, n):
        # I do not have to check top as I forced its initialization
        n.next = self.top
        self.top = n
        self.items += 1

    def pop(self):
        if (not self.top) or (self.items <= 0):
            raise IndexError
        n = self.top
        self.top = self.top.next
        self.items -= 1
        return n

    def peek(self):
        if (not self.top) or (self.items <= 0):
            raise IndexError
        return self.top.data

    # def is_full(s):

class SetOfStacks():
    def __init__(self, stacks=collections.deque(Stack()), threshold = 10):
        self.stacks = stacks
        self.threshold = threshold

    def __repr__(self):
        return f'Set of Stacks ${self.stacks}'

    def push(self, data):
        n = StackNode(data) # Stack() will handle, setting next and top
        if not (self.stacks[0].items < self.threshold): # If no more items in `top` stack
            self.stacks.appendLeft(Stack())
        self.stacks[0].push(n)

    def pop(self):
        if not self.stacks[0]:
            raise Exception()
        n = self.stacks[0].pop()
        if self.stacks[0].items <= 0:
            self.stacks.pop()

    def pop_at(self, index):
        if len(self.stacks) < index:
            raise IndexError()

        n = self.stacks[index].pop()

        if self.stacks[index].items <= 0:
            for i in range(index, len(self.stacks-1)):
                stacks[i] = stacks[i+1]

            stacks.pop()
