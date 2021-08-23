R'''
Write a method to compute all permutations of a string of unique
characters.
'''


def insert_everywhere(s, c):
    R'''
    Helper for brute_force(). Check author's insert_char_at() for a beautiful solution
    '''
    container = []
    len_s = len(s) + 1
    v = ['\n'] * (len_s)
    for k in range(len_s):
        for i in range(len_s):
            if i < k:
                v[i] = s[i]
            elif i > k:
                v[i] = s[i - 1]
            else:
                v[k] = c
        a  = ''.join(v)
        container.append(a)
    return container

def brute_force(s, k = 1):
    R'''
    Works with the same principle as author's first solution, but I couldn't write it recursively.
    '''
    c  = [s[0]]
    v = []
    while k < len(s):
        for p in c:
            t_c = insert_everywhere(p, s[k])
            v += t_c
        c = v
        v = []
        k += 1
    return c


def authors_1(s):
    R'''
    Author's first solution.
    '''
    def insert_char_at(word, c, i):
        start = word[i:]
        end = word[:i]
        a = start + c + end
        return a

    if s == None:
        return None

    permutations = []
    if len(s) == 0:
        permutations.append('')
        return permutations
    if len(s) == 1:
        permutations.append(s)
        return permutations

    first = s[0]
    remainder = s[1:]
    words = authors_1(remainder)
    for word in words:
        for j in range(len(word) + 1):
            s = insert_char_at(word, first, j)
            permutations.append(s)

    return permutations

def authors_2(remainder: str) -> []:
    R'''
    A code for the second solution of author.
    '''
    l = len(remainder)
    result = []

    if l == 0:
        result.append('')
        return result

    for i in range(l):
        before = remainder[:i]
        after = remainder[i+1:]
        partials = authors_2(before + after)

        for s in partials:
            result.append(remainder[i] + s)

    return result

def authors_3(s: str):
    R'''
    A second implementation for author's solution 2.
    '''
    def get_perms(prefix: str, remainder: str, result: []) -> []:
        if len(remainder) == 0:
            result.append(prefix)
        for i in range(len(remainder)):
            before = remainder[:i]
            after = remainder[i+1:]
            c = remainder[i]
            get_perms(prefix + c, before + after, result)

    result = []
    get_perms('', s, result)
    return result

print(brute_force('abc'))
print(authors_1('abc'))
print(authors_2('abc'))
print(authors_3('abc'))
