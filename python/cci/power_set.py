import math

R'''
Write a function that takes as input a set and returns its power set.
'''

def generate_power_set(input_set):
    R'''
    Author's: Brute force
    The number of recursive calls, C(n) satisfies the recurrence C(n) = 2C(n − 1), which solves to C(n) = O(2^n). Since we spend O(n) time within a call, the time complexity is O(n2^n). The space complexity is O(n2^n), since there are 2^n subsets, and the average subset size is n/2. If we just want to print the subsets, rather than returning all of them, we simply perform a print instead of adding the subset to the result, which reduces the space complexity to O(n)
    '''
    # Generate all subsets whose intersection with input_set [0], ...,
    # input_set [ to_be_selected - 1] is exactly selected_so_far .
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        # Generate all subsets that contain input_set[to_be_selected]
        directed_power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])

    power_set = []
    directed_power_set(0, [])

    return power_set

def generate_power_set_opt(s):
    R'''
    Since each set takes O(n) time to compute, the time complexity is O(n2^n). In practice, this approach is very fast.
    '''
    power_set = []
    for int_for_subset in range(1 << len(s)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            pos = int(math.log2(bit_array & ~(bit_array - 1)))
            subset.append(s[pos])
            bit_array &= bit_array-1
        power_set.append(subset)

    return power_set


def power_set(s):
    R'''
    Mine: brute force, iterative though
    '''
    power_set = [[]]

    def add_to_set(i):
        for e in range(len(power_set)):
            print(e)
            power_set.append(power_set[e] + [i])

    for i in s:
        add_to_set(i)

    return power_set


p = generate_power_set_opt(['a', 'b', 3])
print(p)

p = power_set([0, 1, 2])
print(p)
