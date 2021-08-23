

def copy_over(a, b):
    R'''
    Mine. Exactly like author's, from the ideas, to the traps, and all enhancements in between...
    Beautiful.
    '''
    if (a[-1] <= b[0]) or (a[-1] >= b[0]):
        la = len(a)
        for i in range(len(b)):
            a[la + i] = b[i]
        return a

    # From now I will only assume they are sorted in increasing order
    ia, ib = len(a) - len(b) - 1, len(b) - 1
    current = len(a) - 1
    while (ia >= 0) and (ib >= 0) and (current >= 0): # Actually only need ib >= 0
        if a[ia] > b[ib]:
            a[current] = a[ia]
            ia -= 1
            current -= 1
        else:
            a[current] = b[ib]
            ib -= 1
            current -= 1
    if (ia < 0) and (ib >= 0):
        while ib >= 0:
            a[current] = b[ib]
            ib -= 1
            current -= 1
    if (ib < 0) and (ia >= 0):
        if ia == current:
            return a# The elements to copy in a are the elements already in a
        while ia >= 0:
            a[current] = a[ia]
            ia -= 1
            current -= 1
    return a
