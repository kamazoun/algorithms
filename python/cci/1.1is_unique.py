R'''
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def is_unique(s):
    ASCII = 256
    if len(s) > ASCII:
        return False # Pigeon's theorem
    unique = [False]*ASCII
    for i in s:
        if unique[ord(i)]:
            return False
        unique[ord(i)] = True
    return True



def is_unique_without_additional_data_structures(s):
    checker = 0
    for i in s:
        flag = checker & (1 << ord(i))
        if flag:
            return False
        checker = checker | (1 << ord(i))

    return True

 
print(is_unique_without_additional_data_structures(input()))
