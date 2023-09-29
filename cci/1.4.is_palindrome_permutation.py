R'''
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.) 
'''


def is_white_space(c):
    return c == ' ' or c == '\t' or c == '\n'

def is_palindrome_permutation_with_space(s):
    R'''
    O(n) time & O(n) space
    '''
    d = {}

    for i in s:
        d[i] = True

    for i in s:
        d[i] = not d[i]

    count = 0
    for i in s:
        if not d[i] and not is_white_space(i):
            count += 1
            if count > 1: return False

    return True

def is_palindrome_permutation(s):
    R'''
    O(n) time & O(1) space.
    When we use XOR, at any position except the one of the ord() of interested char, all the bits in flag are 0 (1 << ord(x) => 000..00100..00). So at the same position in bit_vector where it's already 0, it will remain 0 and where it's 1 it'll remain 1 (0^0 = 0, 1^1 = 1).
    Only the bit at the `position of the char we are interested in` will switch between 0 and 1 (at the first step it's 0, then 0^1 = 1, then at 2nd step 1^1 = 0, and so on).

    For the bit count, by just substracting 1 from bit_vector, we actually shift its position left (0110 - 1 => 0101). If we were to increment count after that and then substract one again and increment count and so on, count will just end up being the value of bit vector (in previous example, count would be incremented until 6, yet it clearly should be 2).
    To count the 1-s we need to delete them before incrementing count: by substracting then AND-ing (&), we achieve just that. (0110 - 1 => (0101) & (0110) => (0100) and count == 1).

    After re-reading, the previous section might be confusing, so to rephrase:
    * When we delete one from an int, its lowest (close to LSB) bit that is a 1 will be set to 0, and every bit after it until the LSB (that were all 0s) will be set to 1.
      For instance 12 can be represented as `1100` by substracting 1 we have 11 which is `1011`
    * Then, when we do a AND (&) operation of the original bits `1100` and the one from which one was substracted `1011` we actually erase the lowest bit set to 1
      So 1100 & 1011 => 1000
    To sum up bits_vector & (bits_vector - 1) => the lowest bit with value 1 is set to 0
    '''
    bit_vector = 0

    for i in s:
        if is_white_space(i): continue
        flag = 1 << ord(i)
        bit_vector ^= flag # Everywhere it's already 0, it will remain 0 and where it's 1 it'll remain 1. Only the bit at the `position of the char` we are interested in will switch between 0 and 1.

    count = 0
    while bit_vector:
        bit_vector &= bit_vector - 1 # By just substracting 1 from bit_vector, we actually shift its position left. To count the 1s we need to delete them: by substracting then &ing, we achieve just that.
        count += 1

    return count < 2

    
#print(url_ify_in_place(['1', ' ', '\t', '2', '', '', '', '', '', ''], 4))
print(is_palindrome_permutation('la v al '))
