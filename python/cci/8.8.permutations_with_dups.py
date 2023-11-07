R'''
Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.
'''

import collections

def authors(s : str) -> list:
    R'''
    In cases where there are multiple duplicates in the string this is far better than generating all the permutations and removing duplicates.
    '''
    def perms(m : collections.Counter, prefix : str, remaining : int, result : list):
        if remaining == 0:
            result.append(prefix)
            return result

        for (c, count) in list(m.items()):
            if count > 0:
                m[c] -= 1
                perms(m, prefix + c, remaining - 1, result)
                m[c] += 1

    m = collections.Counter(s)
    result = []
    perms(m, '', len(s), result)
    return result

a = authors('aaaaaac')
print(a)
