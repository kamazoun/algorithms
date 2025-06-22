"""
We will build custom stack classes, that will be implemented using a linked list and an using an array.
"""

class StackArray:
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)  
    

    

class StackLinkedList:
    class _StackNode_:
        def __init__(self, value):
            self.value = value
            self.next = None

        

    def __init__(self):
        self.head = None
        self.size = 0


    def push(self, value):
        new_node = self._StackNode_(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.value
    
    def is_empty(self):
        return self.head is None
    
    def size(self): # Because I want it to be the same as the array stack. Otherwise we couldn't call stack.size() on both (here it would be stack.size)
        return self.size
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return self.size
    
