R'''
 Given two strings, write a method to decide if one is a permutation of the other. 
'''


def check_permutation(s1, s2):
    R'''
    O(nlog(n)) time
    '''
    if len(s1) != len(s2): # More than an edge case, without this check, our algorithm doesn't work. Try '123' and '1234'
        return False
    
    s1 = sorted(s1) # Strings do not have a str.sort()
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]: # The first check assures that both strings are of the same length
            return False
    return True


def check_permutation_o_n(s1, s2):
    R'''
    O(n)
    '''
    ASCII = 256
    truth_table = [0] * ASCII
    for i in s1:
        truth_table[ord(i)] += 1
    for i in s2:
        truth_table[ord(i)] -= 1

    for i in truth_table:
        if i != 0:
            return False

    return True


    
print(check_permutation_o_n('123', '1234'))
print(check_permutation_o_n('abc', 'cab'))
print(check_permutation_o_n(input(), input()))
