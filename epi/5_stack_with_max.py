class StackWithMax:

    class MaxWithCount:
        R'''
        This an object to hold the an item and the count of its occurence in the stack
        '''
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self._cached_max_with_count = [] # An auxiliary stack to hold the max elements and their count
        self._stack = [] # The stack itself


    def __repr__(self) -> str:
        return f'StackWithMax(max: {self._max[-1]}, stack: {self._stack})'


    def push(self, item):
        self._stack.append(item)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(item, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if item == current_max:
                self._cached_max_with_count[-1].count += 1
            elif item > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(item, 1))
            # If item < current_max, we do not need to record it, because it will be pop'ed before current_max is

    def pop(self):
        if self.isEmpty(): # Do not forget to check this for pop() and peek()
            raise IndexError('pop(): empty')
        else:
            item = self._stack.pop()
            if item == self._cached_max_with_count[-1].max:
                if self._cached_max_with_count[-1].count > 1:
                    self._cached_max_with_count[-1].count -= 1
                else:
                    self._cached_max_with_count.pop()

            return item


    def peek(self):
        if not self.isEmpty():
            return self._stack[-1]


    def isEmpty(self):
        return len(self._stack) == 0


    def max(self):
        if self.isEmpty:
            raise IndexError('max(): empty')
        return self._cached_max_with_count[-1].max


stack = StackWithMax()
stack.push(1)
stack.push(2)
i = stack.peek()
print(i)
print(stack.)
