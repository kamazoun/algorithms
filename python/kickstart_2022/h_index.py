from sys import stdin
from collections import defaultdict

R'''
At each index i, I want to know if there is i papers with at least i publications.
If not I look for the greatest j < i such that there is j papers with at least j publications.
d[i] += 1

counter = [(index, count of items >= index)]
'''


def solution(c : list) -> str:
    b = []

    last_index = 0
    for index, value in enumerate(c):
        counter = 0
        for i in range(index + 1):
            if c[i] > last_index:
                counter += 1
        if not b or (counter > b[-1][1]):
            last_index = index
        b.append((index, counter))

    print(b)
    r = []
    last = 1
    for index, counter in b:
        if index <= counter:
            r.append(counter)
            last = r[-1]
        else:
            r.append(last)

    return ' '.join(str(r))



    r = [0] * len(c)
    maxi = 0
    for index, value in enumerate(c):
        print(index, value)
        for j in range(index, len(c)):
            if (r[j] <= j) and (j < value): r[j] += 1
            maxi = max(maxi, r[j])
        #r[value] = maxi
        print('maxi est ' , maxi, ' et value ', index)
        r[index] = maxi
        print('r est ' , r)


    return ' '.join(str(r))


r = solution([1, 3, 3, 2, 2, 15])
print(r)
