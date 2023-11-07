R'''
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''

# The algorithm must use character arrays not strings

def is_white_space(c):
    return c == ' ' or c == '\t' or c == '\n'

def url_ify_not_in_place(s, l):
    R'''
    This is kind of a brute force solution. It is O(n), but it is not an in place algorithm.
    '''

    arr = ['']*(len(s)*3)
    z = 0
    for i in range(l):
        if is_white_space(s[i]):
            if is_white_space(s[i+1]): continue # To get rid of continuous (contiguous?) white spaces and only keep one of them
            arr[z] = '%'
            arr[z+1] = '2'
            arr[z+2] = '0'
            z += 3
            print(arr)
        else:
            arr[z] = s[i]
            z += 1
            print(arr)

    return arr


def url_ify_semi_in_place(s, l):
    R'''This algorithm is O(n) and `in place` but still not a beautiful solution though.'''
    
    z = len(s)-1
    #space = len(s)

    for i in reversed(range(l)):
        if not is_white_space(s[i]):
            s[z] = s[i]
            z -= 1
        else:
            if is_white_space(s[i-1]): continue # To get rid of continuous (contiguous?) white spaces and only keep one of them
            s[z], s[z-1], s[z-2] = '0', '2', '%'
            z -= 3

    for i in range(z+1, len(s)):
        print(s[i], end='')
    return s[z+1:]
            


def url_ify_in_place(s, l):
    R'''
    This is a O(n) in-place solution, but writing it on paper was tricky and ultimately a lot of errors occured that were found and corrected in the IDE and after test runs.
    For instance, [duplicata] counts the `total` number of whites while whites counts the `non-adjacent whites` (meaning that if there are 03 whites in a row we will increment whites just by 1, as the 03 whites will be replaced by only one '%20').
    [duplicata] is very important to calculate the final index of each letter (the formula of [z]).
    In addition the position of the checks to see if whites follow each other is also very important. We need to check while counting and also when re-ordering the string to know where to skip.
    '''
    whites = 0
    duplicata = 0

    for i in range(l):
        if is_white_space(s[i]):
            duplicata += 1
            if not is_white_space(s[i+1]): # Condition 1 to get rid of continuous (contiguous?) white spaces and only keep one of them
                whites += 1

    m = 0
    z = whites * 3 + l - duplicata - 1 # -1 because the index starts from 0, z is kind of a length (a position)
    for i in reversed(range(l)):
        if is_white_space(s[i]):
            if is_white_space(s[i-1]): continue # Condition 2, works in tandem with condition 1 above
            s[z], s[z-1], s[z-2] = '0', '2', '%'
            z -= 3
            m += 3
        else:
            s[z] = s[i]
            z -= 1
            m += 1

    for i in range(m):
        print(s[i], end='')
    return s[:m]

    
print(url_ify_in_place(['1', ' ', '\t', '2', '', '', '', '', '', ''], 4))
#print(url_ify_semi_in_place('a\t\tb\n c \t\nd', 11))
