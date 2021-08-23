R'''
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks.
'''


def hanoi(n, origin, target, other):
    R'''
    Mine: Will use list to represent the stack.
    Recursive approach without memoization O(n^2) time O(1) additional space because I am using the same stacks provided at the start of program
    '''
    if n <= 0 or (len(origin) < n):
        raise IndexError('Please provide correct parameters')

    if n == 1:
        plate = origin.pop()
        target.append(plate) # We'll just use list to simulate stacks

    else: # could use return and no else
        hanoi(n - 1, origin, other, target)
        hanoi(1, origin, target, other)
        hanoi(n - 1, other, target, origin)

origin = [1, 2, 3, 4, 5]
target = []
hanoi(5, origin, target, [])
print(target)
