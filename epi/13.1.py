R'''
In this problem you are to count the number of ways of starting at the top-left corner of a 2D array
and getting to the bottom-right corner. All moves must either go right or down.
'''

import collections

def number_of_ways(n, m):
    R'''
    Author's
    The time complexity is O(nm), and the space complexity is O(nm).
    A more analytical way of solving this problem is to use the fact that each path from (0, 0) to (n − 1, m − 1) is a sequence of m − 1 horizontal steps and n − 1 vertical steps. There are combination of (n+m−2) in (n−1) = (n+m−2)! / (n−1)!(m−1)! such paths
    '''
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1

        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
            ways_left = 0 if y == 0  else compute_number_of_ways_to_xy(x, y - 1)
            number_of_ways[x][y] = ways_top + ways_left
            return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]
    return compute_number_of_ways_to_xy(n - 1, m - 1)

def count_recursive_td(n): # nxn matrix
    R'''
        Mine
        O(2^n) I think + stack trace O(n)
        This is the first that I experiment the books' sayings `Recursive algorithms are easier (more natural) to implement that their iterative counterparts`.
        I first tried to solve this iteratively and couldn't even think of a way to put it in code. Next we'll
    '''
    def count_ways(i, j):
        count = 0
        if (i > 0) or (j > 0):
            if j == 0:
                i -= 1
                count +=  count_ways(i, j)
            elif i == 0:
                j -= 1
                count += count_ways(i, j)
            else:
                count += count_ways(i-1, j)
                count += count_ways(i, j-1)
                i -= 1
                j -= 1
            return count
        else:
            return 1

    return count_ways(n-1, n-1)

def count_iterative_td(n):
    R'''
    Mine
    Iterative solution involving a queue (should have been more `softwarey` to use a stack :o)
    Still O(2^n) I think and SURPRISINGLY O(2^n) space I think (more than recursive)
    '''
    i = j = n-1
    q = collections.deque()
    q.append((i, j))
    count = 0
    while q:
        i, j = q.popleft() # Could have use q.pop() to implement a stack to mimic the recursive call stack
        if (i > 0) or (j > 0):
            if j == 0:
                i -= 1
                q.append((i, j))
            elif i == 0:
                j -= 1
                q.append((i, j))
            else:
                q.append((i-1, j))
                q.append((i, j-1))
                i -= 1
                j -= 1
        else:
            count += 1
    return count




R'''
A more analytical way of solving this problem is to use the fact that each path from (0, 0) to (n − 1, m − 1) is a sequence of m − 1 horizontal steps and n − 1 vertical steps. There are combination of (n+m−2) in (n−1) = (n+m−2)! / (n−1)!(m−1)! such paths.
'''
n = count_dp_td(3)
print(n)
