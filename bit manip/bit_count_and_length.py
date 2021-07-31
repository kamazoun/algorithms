R'''
In common usage, the "bit count" of an integer is the number of set (1) bits.
"bit length" counts the actual bit length of a Python integer.
'''

# See https://wiki.python.org/moin/BitManipulation#CA-cefe734dfd2fafec9b326a52e5d6a3ead58b79eb_1

def bitLen(int_type):
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    return(length)

def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)



for i in range(17):
     print(i, bitLen(i))

    
print(is_unique(input()))
t = input()
