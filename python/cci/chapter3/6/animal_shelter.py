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

from cci.node import Node


class Animal:
    def __init__(self, number, type = 'dog'):
        self.type = type
        self.number = number

class AnimalShelter:
    def __init__(self):
        self.dogs = None
        self.cats = None
        self.number = 0

    def enqueue(self, type: str):
        animal = Animal(self.number + 1, type)
        if animal.type == 'dog':
            if self.dogs is None:
                self.dogs = Node(animal)
            else:
                current = self.dogs
                while current.next:
                    current = current.next
                current.next = Node(animal)
            self.number += 1
        elif animal.type == 'cat':
            if self.cats is None:
                self.cats = Node(animal)
            else:
                current = self.cats
                while current.next:
                    current = current.next
                current.next = Node(animal)
            self.number += 1
        else:
            raise ValueError("Animal type must be 'dog' or 'cat'")
        
    def dequeue_any(self):
        if self.number == 0 or (self.dogs is None and self.cats is None):
            raise Exception("No animals in shelter")
        else:
            dog = cat = None
            if self.dogs is not None:
                dog = self.dogs.data
            if not self.cats is None:
                cat = self.cats.data
            if dog and cat:
                if dog.number < cat.number:
                    self.dogs = self.dogs.next
                    self.number -= 1
                    return dog
                else:
                    self.cats = self.cats.next
                    self.number -= 1
                    return cat
            elif dog:
                self.dogs = self.dogs.next
                self.number -= 1
                return dog
            elif cat:
                self.cats = self.cats.next
                self.number -= 1
                return cat


    def dequeue_dog(self):
        if not self.dogs is None:
            dog = self.dogs.data
            self.dogs = self.dogs.next
            self.number -= 1
            return dog
        else:
            print("No dogs in shelter")
            return None
        
    def dequeue_cat(self):
        if not self.cats is None:
            cat = self.cats.data
            self.cats = self.cats.next
            self.number -= 1
            return cat
        else:
            print("No cats in shelter")
            return None
        
    def __repr__(self):
        dogs = []
        cats = []
        current = self.dogs
        while current:
            dogs.append(current.data.number)
            current = current.next
        current = self.cats
        while current:
            cats.append(current.data.number)
            current = current.next
        return f"AnimalShelter(dogs={dogs}, cats={cats}, total={self.number})"
    


if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    print(shelter)
    print("Dequeue any:", shelter.dequeue_any())
    print(shelter)
    print("Dequeue dog:", shelter.dequeue_dog())
    print(shelter)
    print("Dequeue cat:", shelter.dequeue_cat())
    print(shelter)
    print("Dequeue any:", shelter.dequeue_any())
    print(shelter)
    print("Dequeue any:", shelter.dequeue_any())
    print(shelter)
    print("Dequeue any:", shelter.dequeue_any())
    print(shelter) 