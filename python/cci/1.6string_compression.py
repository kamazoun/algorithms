R'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z)
'''


def string_compression(s):
    R'''
    O(n) time of course.
    O(n) space too: The main thing here is that in python the tuples being init'ed the way they are, I need to use the index to print the values to not get and IndexOutOfBounds exception.
    Alternatively, we could init compressed as [(0, 0)]*len(s) and use for (x, y) in compressed: print(x,y,sep). Still the values with 0 would appear, bringing us back to using indexing.
    '''
    compressed = [()] * len(s)
    gains = 0  # The number of chars we get by compressing s
    i, order = 0, 0

    while i < len(s): # TO DO: Fix error in last char
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        consecutive_letters = j - i
        compressed[order] = (s[i], consecutive_letters)
        order += 1
        gains += consecutive_letters - 2
        i = j

    if gains > 0:
        for i in range(((len(s) - gains - 1) // 2)):  # To avoid printing empty elements
            x = compressed[i][0]
            y = compressed[i][1]
            print(x, y, sep='', end='')

    else:
        print(s)


def compression(s: str) -> str:
    R"""
    :param s:
    :return:
    """
    c = s[0]
    count = 0
    d = {}
    order = 0
    for i in s:
        if i == c:
            count += 1
        else:
            d[order] = (c, count)
            order += 1
            count = 1
            c = i
    d[order] = (c, count)
    sl = []  # Avoid concatenating strings
    for i in d.keys():
        sl.insert(i, f'{d[i][0]}{d[i][1]}')

    r = ''.join(sl)
    return r if len(r) < len(s) else s


# print(url_ify_in_place(['1', ' ', '\t', '2', '', '', '', '', '', ''], 4))
print(string_compression('aabcccccaaa'))
print(string_compression('asdfghjkl'))

print(compression('aabcccccaaa'))
print(compression('asdfghjkl'))

assert string_compression('aabcccccaaa') == compression('aabcccccaaa')
assert string_compression('asdfghjkl') == compression('asdfghjkl')
