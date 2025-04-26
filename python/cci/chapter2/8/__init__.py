"""
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value.That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

You can do this in O(A+B) time and 0(1) additional space. That is, you do not need a
hash table (although you could do it with one)
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


def loop(head1: Node, head2: Node) -> Node:
    """
    Using Flyoyd's Tortoise and Hare algorithm to find the intersection point of two linked lists."""
    pass

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

    node5.next = node6
    node6.next = node4  # Intersection at node4

    # intersection_node = intersection(node1, node5)
    # if intersection_node:
    #     print(f"Intersecting Node: {intersection_node.data}")
    # else:
    #     print("No Intersection")
