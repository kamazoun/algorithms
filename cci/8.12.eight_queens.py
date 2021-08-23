R'''
Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.
'''

QUEENS = 8

def print_arr(arr):
    for i in arr:
        print(i)

def mark_and_return_new(arr, row, col, flag = False): # Helper for brute force method
    new_arr = [[] * len(arr[0])] * len(arr) # prep for deep copy

    for i in range(len(arr)): # deep copy of arr in new_arr
        v = [True] * len(arr[i])
        new_arr[i] = v
        for j in range(len(arr[i])):
            new_arr[i][j] = arr[i][j]

    new_arr[row] = [False] * len(arr[row]) # setting whole row to false
    for i in range(len(arr)): # setting whole column to false
        new_arr[i][col] = False

    a = min(row, col)
    r, c = row, col
    row, col = row - a, col - a
    while True: # setting top_left to bottom_right diagonal to false
        if row >= len(arr) or col >= len(arr[row]):
            break
        new_arr[row][col] = False
        row, col = row + 1, col + 1

    r, c = r - r, c + r
    while True: # setting top_right to bottom_left diagonal to false and returning new_arr
        if c >= len(new_arr[0]):
            r, c = r + 1, c - 1
            continue
        if r >= len(new_arr) or c < 0:
            #print_arr(new_arr)
            #print('\n')
            return new_arr
        new_arr[r][c] = False
        r, c = r + 1, c - 1


def brute_force(queens = [], can_place = None, all = []):
    R'''
    This method has SO MANY duplicates: it just reoder the same combination. So there is around A(8, 64)/C(8, 64) times duplicate for each solution
    '''
    if len(queens) == QUEENS:
        print(queens)
        input()
        all.append(queens)
        return

    if None == can_place:
        can_place = [[True] * QUEENS] * QUEENS

    for i in range(QUEENS):
        for j in range(QUEENS):
            if can_place[i][j]:
                new_arr = mark_and_return_new(can_place, i, j)
                brute_force(queens + [(i, j)], new_arr, all)

    return all

def get_positions(rows: list) -> list: # helper for optimized method
    R'''
    Will return a list of the positions (indexes) at which we can place a new queen immediately at the next row in rows (reversed, i.e. from the bottom) so that there is no conflict: namely, at row QUEENS - len(rows) - 1, we will return the indexes where a queen can be placed, so that She is not at conflict with any of a predecessors.
    '''
    positions, i, length = [True] * QUEENS, 0, len(rows) # Could immediately return if rows is empty

    for c in rows:
        positions[c] = False
        drift = length - i
        l, r = c - drift, c + drift
        if l >= 0: positions[l] = False
        if r < QUEENS: positions[r] = False
        i += 1

    return positions

def optimized(rows = [], all = []):
    R'''
    From author's hints.
    The goal here is to place queens from the last row to the first. Thus we only need to keep track to the position of the column at which each queen has been placed (because if we know that we placed 3 queens at rows[7, 6, 5] = 7, 5, 2 ; we know that the placement is (7, 7), (6, 5) & (5, 2)).
    Also to calculate diagonals, we only consider `upper` rows, because the rows in which there is already a queen are already complety `off-limit`.
    In addition the formula for diagonal is:
    x = column +/- (current_row - queen_row), 0 <= x <= QUEENS (7)
    If we place a queen in column c in row 7, in row 6 diags are: c +/- 1, in row five the diags for queen 7 are c +/- 2 (and the diags for row 6 +/- 1).
    '''
    # len(rows) > QUEENS: impossible
    if len(rows) == QUEENS:
        all.append(rows)
        return

    possibilities = get_positions(rows)
    for c in range(len(possibilities)):
        if possibilities[c]:
            optimized(rows + [c], all)

    # return all


result = []
optimized([], result)
print(len(result))
print_arr(result)

input('Enter to launch brute force solution')

result = brute_force()
print(len(result))
