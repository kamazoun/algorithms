R'''
PART ONE
In this problem, you are to implement methods that take a string representing an integer and return
the corresponding integer, and vice versa. Your code should handle negative integers. You cannot
use library functions like stoi in C++, parseInt in Java, and int in Python.
'''

def interconvert_string_to_int(s):
    R'''
    Implement string/integer inter-conversion functions: implement methods that take a string representing an integer and return
the corresponding integer, and vice versa
    '''
    n = 0
    pos = 1
    for i in reversed(range(len(s))):
        if i == 0 and s[i] == '-':
            return -1 * n
        
        x = ord(s[i]) - ord('0')
        if x < 0 or x > 9:
            return
        n += x * pos
        pos *= 10

    return n



def interconvert_int_to_string(n):
    R'''
    Implement string/integer inter-conversion functions: implement methods that take a string representing an integer and return
the corresponding integer, and vice versa
    '''
    x = abs(n)
    s = []
    isNegative = n < 0

    if x == 0:
        return '0' # As our algorithm won't cover this case
    
    while x:
        s.append(str(x%10))
        x //= 10

    if isNegative:
        s.append('-')

    return ''.join(reversed(s))






R'''
PART TWO
Write a program that performs base conversion. The input is a string, an integer b1, and another
integer b2. The string represents an integer in base b1. The output should be the string representing
the integer in base b2.
'''

def base_conversion(s, b1, b2):
    def getVal(c):
        c = c.upper()
        x = ord(c)
        if x >= ord('0') and x <= ord('9'):
            return x - ord('0')
        elif x >= ord('A') and x <= ord('Z'):
            v = x - ord('A')
            return 10 + v

    def setVal(i):
        if 0 <= i and i <= 9:
            return str(i)
        elif 10 <= i and i <= 35:
            return chr(ord('A') + i - 10)

    
    def to_base_ten(s, b):
        p = len(s) - 1
        r = 0
        for i in reversed(range(len(s))):
            r += getVal(s[i]) * (b ** (p-i))
        return r

    def from_base_ten(n, b):
        s = []
        while n:
            s.append(setVal(n % b))
            n //= b

        return ''.join(reversed(s))

    if b1 == 10:
        return from_base_ten(interconvert_string_to_int(s), b2)
    elif b2 == 10:
        return to_base_ten(s, b1)
    else:
        base_ten_val = to_base_ten(s, b1)
        return from_base_ten(base_ten_val, b2)
    
    #print(to_base_ten('1100', 2))
    #print(to_base_ten('ac9', 16))
    #print(from_base_ten(12, 2))
    #print(from_base_ten(2761, 16))

s = interconvert_int_to_string(-2151)
print(s)
n = interconvert_string_to_int('-251450')
print(n)
a = base_conversion('1100', 2, 10)
print(a)
b = base_conversion('12', 10, 2)
print(b)
c = base_conversion('AC9', 16, 10)
print(c)
d = base_conversion('2761', 10, 16)
print(d)
v = base_conversion('kamaz', 25, 17)
print(v)
