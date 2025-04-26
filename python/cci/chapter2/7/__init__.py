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


def authors(head1: Node, head2: Node):
    """
    The solution involves finding the first identical node in the two linked lists (by reference).
    To account for the difference in length, we can traverse the longer list first and then traverse the shorter list. This way, both pointers will be at the same distance from the end of the lists when they meet.
    """
    def length(head: Node) -> int:
        count = 0
        last = None
        while head:
            count += 1
            last = head
            head = head.next
        return count, last
    
    if not head1 or not head2:
        return None
    
    len1, last1 = length(head1)
    len2,last2 = length(head2)
    if last1 is not last2: # If the last nodes are different, the lists do not intersect
        return None
    
    # Move the pointer of the longer list ahead by the difference in lengths
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next
    # Traverse both lists together until the intersection point is found
    while head1 and head2:
        if head1 is head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None



def intersection(head1: Node, head2: Node) -> Node:
    """
    Using Flyoyd's Tortoise and Hare algorithm to find the intersection point of two linked lists."""
    l1, l2 = head1, head2
    if not l1 or not l2:
        return None
    while l1.next:
        l1 = l1.next
    l1.next = l2
    
    slow, fast = l1, l1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    slow = l1
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow

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

    intersection_node = intersection(node1, node5)
    if intersection_node:
        print(f"Intersecting Node: {intersection_node.data}")
    else:
        print("No Intersection")
