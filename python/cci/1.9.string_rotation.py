R"""
String Rotation:Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat")
"""


def is_rotation(s1: str, s2: str) -> bool:
    R"""
    We use a hint from the author:
    What happens when we concatenate s1 or s2 with itself.
    :param s1: One of the strings
    :param s2: The other string
    :return: A boolean indicating whether s1 and s2 are rotations of each other.
    """
    def is_substring(full_string: str, substring: str) -> bool:
        if len(substring) > len(full_string):  # Not necessary
            return False
        return substring in full_string
    if is_substring(s2*2, s1):
        return True
    return False


s1 = 'waterbottle'
s2 = 'erbottlewat'

r = is_rotation(s1, s2)
print(r)