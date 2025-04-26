"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input:A - > B - > C - > D - > E - > C [the same C as earlier]
Output:C
"""


# my_python_project/python/cci/problem2/6is_palindrome.py
import sys
import os
# Step 1: Determine the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Step 2: Determine the project root directory
# Adjust the number of '../' based on your projectstructure
project_root = os.path.abspath(os.path.join(current_dir, '../../..'))
print("We are currently here: ", project_root, '\n')
# Step 3: Add the project root to sys.path if it'snot already there
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print("Added the project root to sys.path")
else:
    print("Project root is already in sys.path")

# Step 4: Perform the import using absolute paths
from cci.chapter2.node import Node


def loop(head: Node) -> Node:
    """
    Using Flyoyd's Tortoise and Hare algorithm to find the intersection point of two linked lists."""
    if not head:
        return None
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Collision point
            break
    else:
        return None  # No loop
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast
    

if __name__ == "__main__":
    # Example Usage
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    # Creating two intersecting linked lists
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node4  # Intersection at node4

    intersection_node = loop(node1)
    if intersection_node:
        print(f"Intersecting Node: {intersection_node.data}")
    else:
        print("No Intersection")
