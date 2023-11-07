import Collections

R'''
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''

MinNode = Collections.namedtuple('MinNode', ['value', 'count'])

class StackMin():
    class StackNode():
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def __repr__(self):
            return f'StackNode({self.data})'



    def __init__(self, top=None):
        self.top = top
        self.min = StackNode(MinNode(float('inf'), 1), None)


    def push(self, data):
        node = StackNode(data, self.top)
        self.top = node

        current_min_node = self.min.data # MinNode
        if data < current_min_node.value:
            new_min_node = MinNode(data, 1)
            new_min = StackNode(new_min_node, self.min)
            self.min = new_min
        elif data == current_min_node.value:
            self.min.data.count += 1
        # if data > current min we do not push it to the stack

    def pop(self):
        if not self.top:
            raise KeyError('error occured')

        node = self.top
        self.top = self.top.next

        current_min_node = self.min.data # MinNode
        if node.data == current_min_node.value: # It cannot be less, equal or greater. For greater, we don't care
            if current_min_node.count >= 2:
                self.min.data.count -= 1
            else:
                slef.min = self.min.next

    def min(self):
        if top:
            return self.min.data.value
