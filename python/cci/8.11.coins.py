R'''
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.
'''
import collections

def authors():
    pass

def coins(n: int, m = [], ht = []) -> []:
    if n < 0: return 0
    index = ''.join(sorted(m))
    if n == 0:
        ht[index] = 1
        return
    if ht[index] != 0:
        return


    coins(n - 1, m + ['1'], ht)
    coins(n - 5, m + ['5'], ht)
    coins(n - 10, m + ['10'], ht)
    coins(n - 25, m + ['25'], ht)

    result = [i for i in ht.keys() if ht[i] == 1]
    return result

ht = collections.defaultdict(int)
c = coins(7, ht = ht)
print(c)
print(len(c))
