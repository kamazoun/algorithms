R'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''

from typing import List

def rotate_matrix_auth(m):
    R'''
    This is the author solution: it involves actually 'rotating' the rows and columns 'layer by layer'. After implementing my method below and seeing this, it seems naive.
    Here too, remember to only go up to n//2 (range(n//2 + 1))
    '''
    n = len(m)

    for layer in range(n//2 + 1):
        start = layer # In the first layer we start a 0 (m[0][0], ...), in the second we start at 1 (m[1][1])
        end = n - layer - 1 # In the first layer we start at n-1 (for n = 3, m[2][x], ...), in the second layer we start at n-2 (m[1][x])
        for i in range(layer, n//2+1):
            reverse = n - i - 1
            m[i][end], m[end][reverse], m[reverse][start], m[start][i] = m[start][i], m[i][end], m[end][reverse], m[reverse][start]



def rotate_matrix(m):
    R'''
    In place (O(1) space) and O(n2) time.
    The trick was just to find how to rotate: my technique was
    1: mirror according to the diagonal from bottom-left to top-right (be careful though, swapping all the elements will make the matrix appear not to have changed, bc elements already swapped are re-swapped and put back to place. We need to swap in range(n//2 + 1)).
    2: mirror according to middle row horizontally: Here to only up to n//2 (range(n//2 + 1))
    '''
    n = len(m)

    for i in range(n//2+1):
        for j in range(n//2+1):
            m[i][j], m[n-j-1][n-i-1] = m[n-j-1][n-i-1], m[i][j]

    for i in range(n//2):
        m[i], m[n-i-1] = m[n-i-1], m[i]

    # return m in place


def rotate(m: List) -> None:
    a = len(m) - 1
    for depth in range(len(m) // 2):
        r = len(m[depth]) - depth - 1 # because r is used in the matrix subscript and thus without a -1 an IndexOutofBound would be thrown.
        for i in range(depth, r + 1): # Because range is exclusive at the end, so will end at r.
            print(f'Case {i}')
            t = m[depth][i]
            m[depth][i] = m[a - i][depth]
            m[a - i][depth] = m[a - depth][a - i]
            m[a - depth][a - i] = m[i][r]
            m[i][r] = t
            grid_print(m)




def grid_print(m):
    for row in m:
        print(row)
    print('\n\n')

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
grid_print(m)
rotate(m)
grid_print(m)