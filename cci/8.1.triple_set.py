import collections

R'''
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
'''

def triple_set(n, d = collections.defaultdict(int)):
    if n <= 2:
        if n != 0 and d[n] == 0:
            d[n] = n
        return d[n]
    else:
        d[n] = triple_set(n - 3, d) + triple_set(n - 2, d) + triple_set(n - 1, d)
        return d[n]

n = triple_set(int(input()))
print(n)
