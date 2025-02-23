# my_python_project/python/cci/problem2/6is_palindrome.py
import sys
import os
# Step 1: Determine the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Step 2: Determine the project root directory
# Adjust the number of '../' based on your projectstructure
project_root = os.path.abspath(os.path.join(current_dir, '../../..'))
print("We are current here: ", project_root, '\n')
# Step 3: Add the project root to sys.path if it'snot already there
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print("Added the project root to sys.path")
else:
    print("Project root is already in sys.path")

# Step 4: Perform the import using absolute paths
from cci.chapter2.node import Node

def is_palindrome(head: Node) -> bool:
    pass
    


if __name__ == "__main__":
    # Example Usage
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(1)
    node1.next = node2
    node2.next = node3
    print(is_palindrome(node1))  # Output: True








# from cci.chapter2.node import Node
 

# def is_palindrome(head: Node) -> bool:
#     print('fewr')