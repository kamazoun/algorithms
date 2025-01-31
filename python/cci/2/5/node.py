from typing import List


class Node:
    def __init__(self, data: int, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data}"
    
    def traverse(self):
        current = self
        while current:
            print(current.data, end=" --> ")
            current = current.next


def build_linked_list(data: List) -> Node:
    head = None
    node = None
    prev = None
    for i in data:
        node = Node(i)
        if prev:
            prev.next = node
        else:
            head = node
        prev = node
    return head

"""
Here is what I got from a conversation with Gemini:
When you assign another node to the next parameter of a node in a linked list, what's actually stored is a reference (or a pointer).  
You're not copying the entire data of that node. Instead, you're essentially creating a shorthand that directly points to the memory location of the next node.

Member Access with `.`: When you use code like first_node.next.data, Python first dereferences the next pointer in the first node. It retrieves the memory location stored there and follows that location to access the actual next node.
Automatic Dereferencing: Python then recognizes that data is an attribute of the retrieved node and uses the value stored in that node's data attribute.
"""