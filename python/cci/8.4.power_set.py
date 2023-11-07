R'''
Write a method to return all subsets of a set.


We should first have some reasonable expectations of our time and space complexity.
How many subsets of a set are there? When we generate a subset, each element has the "choice" of either
being in there or not. That is, for the first element, there are two choices: it is either in the set or it is not. For
the second, there are two, etc. So, doing { 2 * 2 * . . . } n times gives us 2^n subsets.
Assuming that we're going to be returning a list of subsets, then our best case time is actually the total
number of elements across all of those subsets. There are 2^n subsets and each of the n elements will be
contained in half of the subsets (which 2^n-1 subsets). Therefore, the total number of elements across all of
those subsets is n * 2^n-1.
We will not be able to beat 0(n2^n) in space or time complexity.
'''
import math

def power_set(s):
    R'''
    Mine: Simple O(n2^n) time and space
    '''
    if not s:
        return None

    power_set = [[]]
    for i in s:
        n = [] # Could use the index in pset to avoid using additional variable
        for pset in power_set:
            n.append(pset + [i])
        power_set += n

    return power_set

def power_set_optimized(s):
    R'''
    Still O(n2^n) time but using a bit array.
    '''
    if not s: return None
    power_set = []

    for int_set in range(1 << len(s)): # 0 ~ 2^n - 1
        bit_array = int_set
        subset = []
        while bit_array:
            pos = int(math.log2(bit_array & ~(bit_array - 1)))
            subset.append(s[pos])
            bit_array &= (bit_array - 1)
        power_set.append(subset)

    return power_set

p = power_set([0, 1, 2])
print(p)

p = power_set_optimized(['a', 'b', 'c'])
print(p)
