import itertools

def find_max_sub_array(a):
    R'''
    Author's
    '''
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(a):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)

    return max_sum

arr = [100, 50, 25, 85, -3560, -3, 105, 102, 86, -63, 81, -2050, 101, 94, -50, 106, 101, -508, 79, 94, 90, 97]
a = find_max_sub_array(arr)
print(a)
