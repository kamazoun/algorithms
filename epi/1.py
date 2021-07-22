R'''
Write expressions that use bitwise operators, equality checks, and Boolean operators to do
the following in O(1) time.
• Right propagate the rightmost set bit in x, e.g., turns (01010000)2 to (01011111)2.
• Compute x modulo a power of two, e.g., returns 13 for 77 mod 64.
• Test if x is a power of 2, i.e., evaluates to true for x = 1, 2, 4, 8, . . . , false for all other values.
'''



def right_propagate_rmb(x):
    R'''Right propagate the rightmost set bit in x, e.g., turns (01010000)2 to (01011111)2.'''
    return x | (x - 1)

def modulo_power(x, power):
    R'''Compute x modulo a power of two, e.g., returns 13 for 77 mod 64.'''
    return x & ~(2**power)

def test(x):
    R'''Test if x is a power of 2, i.e., evaluates to true for x = 1, 2, 4, 8, . . . , false for all other values.'''
    return (x != 0) and (x == (x & ~(x - 1)))


a = right_propagate_rmb(int('01010000', 2))
print(bin(a))

b = modulo_power(77, 6)
print(b)

c = test(0)
print(c)

d = test(1)
print(d)
