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

def is_palindrome(head: Node) -> bool:
    # Step 1: Find the middle of the linked list using the fast and slow pointer technique
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Step 2: Reverse the second half of the linked list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    # Step 3: Compare the first half and the reversed second half
    first_half = head
    second_half = prev
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True
    


if __name__ == "__main__":
    # Example Usage
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(1)
    node1.next = node2
    node2.next = node3
    print(is_palindrome(node1))
    node4 = Node(1)
    node5 = Node(2)
    node6 = Node(2)
    node7 = Node(1)
    node4.next = node5
    node5.next = node6
    node6.next = node7
    print(is_palindrome(node4))









# from cci.chapter2.node import Node
 

# def is_palindrome(head: Node) -> bool:
#     print('fewr')