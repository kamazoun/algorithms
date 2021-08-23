R'''
You have an integer and you can flip exactly one bit from a O to a 1. Write code to find the length of the longest sequence of 1 s you could create.
EXAMPLE
Input: 1775
Output: 8
'''
import math

def find_largest_sequence(arr, l, r):
    R'''
    Helper function to get the length of the largest sequence.
    The problem with these implementations is that, although I tought out the logic and simulated the code with test values, they will probably be some errors if I ran it on an IDE. This is not algorithmic code
    '''
    if not arr or l > r:
        return 0

    if l == r:
        return 1 if arr[l] == 1 else 0

    mid = l + (r - l) // 2
    a = find_largest_sequence(arr, l, mid - 1)
    b = find_largest_sequence(arr, mid + 1, r)

    if (mid - 1) >= 0 :
        v  = arr[mid - 1]
    else:
        v = 0
    if (mid + 1) < len(arr) :
        t  = arr[mid + 1]
    else:
        t = 0

    y = v + t + arr[mid]

    if y == 0:
        return max(a, b) + 1
    elif y == 1:
        return max(a, b) + arr[mid]
    elif y == 2:
        return a + b + 1
    else:
        x = a + b
        if x <= r:
            return x + 1
        else:
            return x

def flip_to_win(n):
    R'''
    DOESN'T WORK
    Mine: O(b) time and space, with b the length of the bit_array
    '''
    bit_array = get_bit_array(n)
    print(bit_array)
    return find_largest_sequence(bit_array, 0, len(bit_array) - 1)

def flip_to_win_algorithmic(n: int) -> int:
    R'''
    Author's: One of the most beautiful algorithms I have seen.
    O(log(b)) time and O(1) space. b: number of bits to represent n
    '''
    assert n >= 0, 'Provide a positive integer please' # No parentheses in python asserts?
    # Very important base case, if not alg doesn't work
    if (~n) == 0: # All 1s
        return len(get_bit_array(n))

    current_len = previous_len = 0
    max_len = 1

    while n != 0:
        if (n & 1) == 1:
            current_len += 1
        elif (n & 1) == 0:
            previous_len = 0 if (n & 2 == 0) else current_len
            current_len = 0
        max_len = max(max_len, current_len + previous_len + 1) # +1 because there will always be a 0 in the bit_array representing n.
        n >>= 1

    return max_len



def get_bit_array(n):
    R'''
    Helper function

    bit_array = [0] * (int(math.log2(n)) + 1)
    k = 0
    while n > 0:
        bit_array[k] = n % 2
        n = n // 2
        k += 1

    return bit_array
    '''
    bit_array = [0] * (int(math.log2(n)) + 1)
    while n > 0:
        b = int(math.log2(n))
        bit_array[b] = 1
        n -= 2**b

    return bit_array


a = flip_to_win_algorithmic(1775)
print(a)
