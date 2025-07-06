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
from cci.common_ds import DoubleNode
from cci.node import Node

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type  # 'dog' or 'cat'
        self.next = None

    def __repr__(self):
        return f"{self.type.capitalize()}({self.name})"

class AnimalShelter:
    def __init__(self):
        self.all = DoubleNode()
        self.dogs = Node()
        self.cats = Node()

    def enqueue(self, animal: Animal):
        self.all.append(animal)
        if animal.type == 'dog':
            self.dogs.append(animal)
        elif animal.type == 'cat':
            self.cats.append(animal)

    def dequeue_any(self):
        if self.all.is_empty():
            raise Exception("No animals in shelter")
        #animal = self.all.remove_first()
        #if animal.type == 'dog':
        #     self.dogs.remove(animal)
        # elif animal.type == 'cat':
        #     self.cats.remove(animal)
        # return animal

    def dequeue_dog(self):
        if self.dogs.is_empty():
            raise Exception("No dogs in shelter")
        # dog = self.dogs.remove_first()
        # self.all.remove(dog)
        # return dog