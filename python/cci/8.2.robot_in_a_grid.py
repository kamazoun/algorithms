R'''
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
'''

class BTNode():
    def __init__(self, data, left = None, top = None, parent = None):
        self.data = data
        self.left = left
        self.top = top
        self.parent = parent

    def __repr__(self):
        return f'BTNode(data = ${self.data}, left = ${self.left}, top = ${self.top})'


def find_path(arr, r, c):
    R'''
    DOESN'T WORK.
    I went with a binary tree, complicated the code, and finally it doesn't work
    '''
    def recurse(i, j, parent):
        if arr[i][j] == False: # Off limit
            return False

        if (i == 0) and (j == 0):
            tree = BTNode((i, j), parent = parent)
            path = []
            p = tree
            while p.parent:
                path.append(p.data)
                p = p.parent
            print(path)
            #for p in path:
                #print(p)
            return False

        tree = BTNode((i, j), parent = parent)
        l = False if j <= 0 else recurse(i, j-1, tree)
        t = False if i <= 0 else recurse(i-1, j, tree)
        #tree.left = l
        #tree.right = r
        return l or t

    if c <= 0 and r <= 0:
        return (c, r)

    is_path = recurse(r-1, c-1, None)
    print(is_path)



def find_path_auth(maze):
    R'''
    Author's
    O(rows*cols). Her algorithm is so beautiful. Without memoization it's O(2^col+row) though.
    '''
    def get_path(maze, row, col):
        if (col < 0) or (row < 0) or (not maze[row][col]):
            return False
        if (row, col) in failed_points:
            return False

        isAtOrigin = (row == 0) and (col == 0)

        if isAtOrigin or get_path(maze, row, col - 1) or get_path(maze, row - 1, col):
            path.append((row, col))
            return True

        failed_points.add((row, col))
        return False


    if not maze or (len(maze) == 0):
        return None

    path = []
    failed_points = set()

    if get_path(maze, len(maze) - 1, len(maze[0]) - 1):
        return path

    return None



a = [[True, True, True, False], [True, True, False, True], [True, True, True, True], [False, True, True, True]]
#find_path(a, 4, 4)
p = find_path_auth(a)
print(p)
