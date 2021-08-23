R'''
Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print 'ERROR.'
'''
import math

def for_ints(n):
    bit_array = [0] * (int(math.log2(n)) + 1)
    while n > 0:
        b = int(math.log2(n))
        bit_array[b] = 1
        n -= 2**b

    return bit_array


def bin_to_str(n):
    R'''
    Mine.
    Author's methods seem better
    '''
    n2 = int(n)
    while n != n2:
        n *= 10
        n2 = int(n)

    if n2 > (2 ** 32) - 1:
        return 'ERROR.'

    bit_array = for_ints(n2)
    return '0.' + ''.join(str(i) for i in bit_array)


def bin_to_str_auth1(n):


n = bin_to_str(0.12)
print(n)
