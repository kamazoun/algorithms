R'''
Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
'''

import math

def mul(a: int, b: int) -> int:
    R'''
    Mine: O(log(x)) time and O(1) space, x = min(a, b)
    I feel my solution is more beautiful than author's, although hers reminded me of the base cases (that would have been handled anyway)
    '''
    assert (a >= 0) and (b >= 0), 'Provide positive integers please'

    # I took out the base cases as our solution handles them, it'd just make the code more `bushy`

    x = min(a, b)
    y = max(a, b)

    result = 0

    while x > 0:
        b = int(math.log2(x))
        t_y = y
        result += t_y << b
        x -= 1 << b

    return result


c = mul(170, 250)
print(c)
