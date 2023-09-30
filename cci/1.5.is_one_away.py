R'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
'''

from typing import Optional


def is_one_away(a, b):
    R"""
    O(n)time and space.
    The challenge in that implementation is to be careful with the branching conditions. Logically it's simple, but it can be confusing.
    If we reach the end of string b, yet not the end of a, there is 1 (and only one, the first check makes sure we have one unit of length difference at most and the [diff] variable would return if two differences were already encountered) more char in a, so one more difference. We make sure that there were no other differences before that one.
    """
    if abs(len(a) - len(b)) > 1:
        return False

    j = 0
    diff = 0
    for i in range(len(a)):
        if j >= len(b):
            return diff + 1 <= 1

        if a[i] == b[j]:  # Normal case. Char are the same
            j += 1
            continue  # Not needed, just to make clear

        elif a[i + 1] == b[j]:  # A char has been inserted in a at index i
            diff += 1

        elif a[i] == b[j + 1]:  # A char has been inserted in b at index i
            diff += 1
            j += 2

        elif a[i + 1] == b[j + 1]:  # A char has been replaced in one of the strings at index i
            diff += 1
            j += 1

        if diff > 1:
            return False

    return True


# print(url_ify_in_place(['1', ' ', '\t', '2', '', '', '', '', '', ''], 4))
print(is_one_away('pale', 'ple'))
print(is_one_away('pales', 'pale'))
print(is_one_away('pale', 'bale'))
print(is_one_away('pale', 'bake'))
print(is_one_away('ple', 'pale'))
print(is_one_away('ple', 'pal'))
print(is_one_away('al', 'pal'))

