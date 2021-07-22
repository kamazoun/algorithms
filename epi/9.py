import collections

def is_constructible(l, m):
    if not l or not m:
        return False

    if len(l) > len(m):
        return False

    d_l = collections.defaultdict(int)
    d_m = collections.defaultdict(int)

    for c in l:
        d_l[c] += 1

    for c in m:
        d_m[c] += 1

    for k in d_l.keys():
        if d_l[k] > d_m[k]: # If d_m[k] doesn't it value will be 0 instead of throwing KeyError like a normal dict
            return False

    return True



def is_constructible_the_pythonic_way(l, m):
    if len(l) > len(m):
        return False

    d_l = collections.Counter(l)
    d_m = collections.Counter(m)

    r = (d_l - d_m)

    #Works too: return all(None for c in r.values())#The same as: all(c == None for c in r.values())
    return not r # Although r is still a Counter, when it is empty not r returns True

l = 'vfsgfusbns'
m = 'gfjnbkjdfb'

a = is_constructible(l, m)
print(a)


l = 'asdffdfdafa'
m = 'fasfasfdafdasafasfsafadfasfafasfsada'

a = is_constructible(l, m)
print(a)

a = is_constructible_the_pythonic_way(l, m)
print(a)
