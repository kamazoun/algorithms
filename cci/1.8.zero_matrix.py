R'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
'''

from typing import List

def zero_matrix(a, m, n):
    R'''
    My first `reasonnable` approach. Although I feel it is not good.
    O(M^2N + MN^2) time just for O(1) space :(. It's not good. We can make it O(MN) with O(M + N) space.
    Here, the obvious errors I nearly made were: 1. To think that once I find a zero on a row I just have to zero the remaining values: Nope, I have to circle through all of them to  zero their column
    2. I also have to zero left from a zero's row, and up from a zero's column.
    '''
    if not a:
        return

    for i in range(m):
        for j in range(n):
            if a[i][j] == 0:
                k = 0
                while k < n:
                    if a[i][k] != 0:
                        a[i][k] = float('inf')
                    k += 1
                l = 0
                while l < m:
                    if a[l][j] != 0:
                        a[l][j] = float('inf')
                    l += 1

    for i in range(m):
        for j in range(n):
            if a[i][j] >= float('inf'):
                a[i][j] = 0

    return a


def zero_matrix_auth(a, m, n):
    R'''
    Based off author's, `optimized` solution. I feel like neither her nor I can decently solve this problem.
    O()
    '''

    def nullify_column(j):
        for i in range(1, m):
            a[i][j] = 0

    def nullify_row(i):
        for j in range(1, n):
            a[i][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if a[i][j] == 0:
                a[0][j] = 0
                a[i][0] = 0

    for i in range(1, m):
        if a[i][0] == 0:
            nullify_row(i)

    for j in range(1, n):
        if a[0][j] == 0:
            nullify_column(j)

    set_origin = False

    print(a)

    if a[0][0] == 0:
        nullify_column(0)
        nullify_row(0)
        set_origin = True
    else:
        for j in a[0]:
            if j == 0:
                set_origin = True # Be very careful, the column has already been set to 0,the ROW SHOULD NOT, only (0,0)
        for i in range(m):
            if a[i][0] == 0:
                set_origin = True # Be very careful, the row has already been set to 0,the COLUMN SHOULD NOT, only (0,0)

    if set_origin:
        a[0][0] = 0

    return a


def matrix_zero(a: List):
    def zero_row(r):
        pass

    def zero_column(c):
        pass

    rows_to_zero = []
    columns_to_zero = []
    m = len(a)
    for i in range(m):
        n = len(m[i])
        for j in range(n):
            if a[i][j] == 0:
                rows_to_zero.append(i)
                columns_to_zero.append(j)

    for r in rows_to_zero:
        zero_row(r)

    for c in columns_to_zero:
        zero_column(c)


a = [[1, 2, 0], [6, 5, 4], [7, 0, 9]]
a = zero_matrix_auth(a, len(a), len(a[0]))
print(a)
