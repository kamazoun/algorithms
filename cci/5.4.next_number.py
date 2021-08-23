R'''
Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.
'''
import math
'''
There is the particular case where the bits fill the max length in the language: 1111..1100..0000. It is not possible to extend the number above that (ex. 32 bits used in java).
Python does not have this problem as there is no limit to the size of the bit_array
'''
# I will print the results of all the functions to be able to compare results

def authors(n):
    R'''
    This uses an arithmetic approach to the problem
    '''
    def get_next(n):
        R'''
        c0 is the number of trailing zeros
        cl is the size of the one block immediately following.
        '''
        c0 = c1 = 0
        while True:
            if n & (1 << c0):
                break
            c0 += 1
        c1 = c0
        while True:
            if n & (1 << c1):
                c1 += 1
                continue
            break
        c1 -= c0

        return n + (1 << c0) + (1 << (c1 - 1)) - 1

    def get_previous(n):
        R'''
        c1 is the number of trailing ones
        c0 is the size of the zero block immediately following
        '''
        c0 = c1 = 0
        while True:
            if n & (1 << c1):
                c1 += 1
                continue
            break
        c0 = c1
        while True:
            if n & (1 << c0):
                break
            c0 += 1

        return n - (1 << c1) - (1 << (c0 - 1)) + 1

    previous, next = get_previous(n), get_next(n)
    print(previous, n, next)

def brute_force(n):
    R'''
    I wrote it to verify future results and have a better understanding of the traps in this problem.
    '''
    bit_array = get_bit_array(n)
    n_count = sum(bit_array)

    next = previous = n

    while True:
        next += 1
        t = sum(get_bit_array(next))
        if t == n_count:
            break

    while previous > 0:
        previous -= 1
        if previous == 0:
            previous = None
            break
        t = sum(get_bit_array(previous))
        if t == n_count:
            break

    print(f'{previous}:{get_bit_array(previous)}, {n}:{get_bit_array(n)}, {next}:{get_bit_array(next)}')





def next_number(n):
    R'''
    Helper function to get next number
    '''
    trailing_zeroes = 0
    while True:
        if n & (1 << trailing_zeroes):
            break
        trailing_zeroes += 1

    pos_nt_zero = trailing_zeroes # position of the first non-trailing 0
    while True:
        if n & (1 << pos_nt_zero):
            pos_nt_zero += 1
            continue
        break

    n |= (1 << pos_nt_zero)
    n &= -1 << (pos_nt_zero)
    ones = (pos_nt_zero - 1) - (trailing_zeroes + 1)
    n |= 1 << (ones + 1)
    n -= 1

    return n


def previous_number(n):
    R'''
    Helper function to get previous number
    '''
    if n == 0 or ~n == 0:
        return None

    t = n
    ones = 0 # Ones before zeros if LSB is a 1. Ex 100111011 ones = 2
    zeros = 0 # Zeros before `first` one (not counting LB). Ex 1010011 zeros = 2

    while True:
        if t & (1 << ones):
            ones += 1
        else:
            zeros = ones + 1
            break

    while True:
        if t & (1 << zeros):
            break
        zeros += 1

    number_of_zeros_to_shift = zeros - ones - 1
    mask = -1 << (zeros)
    t &= mask # Zeroes everything after the first non-trailing 1 and till the lsb
    previous = t - 1 # zeroes first non-trailing 1  and ones everything after until lsb
    mask = -1 << (number_of_zeros_to_shift)
    previous &= mask

    return previous

def previous_next_numbers(x):
    R'''
    A lot of off-by-one errors, and understanding the difference between the `position` of a bit and its `index`. Counts start at 0. Shifts of 0 have no effects.
    The secret of solving this problem optimally is to figure out that we do not need to consider so many cases, but only if the bit we are interested in is non-trailing or not.
    '''
    p = previous_number(x)
    print(p, end = ' ')
    print(x, end = ' ')
    n = next_number(x)
    print(n)

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
    if not n:
        return None
    bit_array = [0] * (int(math.log2(n)) + 1)
    while n > 0:
        b = int(math.log2(n))
        bit_array[b] = 1
        n -= 2**b

    return bit_array


brute_force(486)
previous_next_numbers(486)
authors(486)
