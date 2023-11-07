R'''
Write a method to sort an array of strings so that all the anagrams are next to each other.
'''
import collections


def group_anas(s):
    R'''
    Mine: O(n(ilog(i) + 1)) => O(n*ilog(i)) and O(n) space, i: length of longest anagram, n number of anagrams in s
    '''
    ht = collections.defaultdict(list)
    for ana in s: # O(n)
        t = ''.join(sorted(ana)) # O(ilogi) i: length of longest anagram
        ht[t].append(ana)

    k = 0
    for i in ht.keys(): # O(n)
        values = ht[i]
        for v in values:
            s[k] = v
            k += 1

    return s


def group_optimized(s):
    R'''
    By using a bit more space to store the bit array [alphabetic_count], we managed to reduce the alg to O(n(i + 1)) => O(ni) with still O(n) space
    '''
    ht = collections.defaultdict(list)

    for ana in s: # O(n)
        alphabetic_count = 0
        for i in ana.lower(): # O(i) instead of O(ilogi)
            k = ord(i) - 97 # assumes only chars
            alphabetic_count |=  1 << k
        ht[alphabetic_count].append(ana)

    k = 0
    for key in ht.keys(): # O(n)
        values = ht[key]
        for v in values:
            s[k] = v
            k += 1

    return s

s = ['laval', 'bac', 'taxi', 'cab', 'valla']
v = group_optimized(s)
print(v)
