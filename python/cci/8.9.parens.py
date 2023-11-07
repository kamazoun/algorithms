R'''
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
EXAMPLE
Input: 3 Output: ( ( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
'''

def mine_bit_array(n):
    R'''
    The idea is to generate all numbers until 2^(n + 1) - 1 then replace 1 by '(' and 0 by ')', for those that fullfil the following conditions:
    1. The numbers of 0s and 1s must be equal
    2. From the msb the count of 0 must never exceed the count of 1s {the number bit_array cannot start with a 0 => ')' }, inversely from the lsb the count of 1s must never exceed the count of 0s {the number cannot end with a 1 => '(' }.
    While writing this, I figured that if I represented '(' with 0 and ')' with one, I would need to generate a bit less numbers as the first one would always be a 0.
    '''
    for max in range(2**(2*n)):
        ones = zeros = 0
        bit_arr = []
        #print(max)
        while max:
            if max & 1:
                ones += 1
                bit_arr = [1] + bit_arr
            else:
                zeros += 1
                bit_arr = [0] + bit_arr
            if ones > zeros:
                break
            max >>= 1
        if ones == zeros == n:
            v = ''.join(')' if i == 0 else '(' for i in bit_arr)
            print(v)


def mine_recursive(ones, zeros, result = ''): # for n parentheses: ones == zeros == n
    if zeros < ones:
        return
    if ones <= 0:
        for i in range(zeros):
            result += ')'
        print(result)
        return

    mine_recursive(ones - 1, zeros, result + '(')
    mine_recursive(ones, zeros - 1, result + ')')


##### A VERY FUNNY THING IS THAT THE TWO IMPLEMENTATION RESULTS ARE SYMMETRIC BY THE LINE -----------
mine_bit_array(3)
print('---------')
mine_recursive(3, 3)
