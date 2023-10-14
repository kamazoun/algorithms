R"""
String Rotation:Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat")
"""


def is_rotation(s1: str, s2: str) -> bool:
    def is_substring(full_string: str, substring: str) -> bool:
        if len(substring) < len(full_string):  # Not necessary
            return False
        return substring in full_string
    pass
