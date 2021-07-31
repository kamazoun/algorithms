R'''
Suppose that you been offered the opportunity to invest in the Volatile Chemical
Corporation. Like the chemicals the company produces, the stock price of the
Volatile Chemical Corporation is rather volatile. You are allowed to buy one unit
of stock only one time and then sell it at a later date, buying and selling after the
close of trading for the day. To compensate for this restriction, you are allowed to
learn what the price of the stock will be in the future. Your goal is to maximize
your profit.
'''


def max_middle_array(arr, low, middle, high):
    R'''
    The goal is to find the maximum subarray that spans around `middle`, i.e from low <= middle < high.
    The technique is to find the maximum to the left of middle and the maximum to the right of middle then combine then.
    Returns the lower and upper bounds of the found subarray (both inclusive from the range low ~ high-1)
    '''
    left_max = float('-inf') # Will hold the maximum sum for left of middle subarray
    left_index = low
    sum = 0
    for i in reversed(range(low, middle)): # middle not included in left side
        sum += arr[i]
        if sum > left_max:
            left_max = sum
            left_index = i

    right_max = float('-inf') # Will hold the maximum sum for right of middle subarray
    right_index = middle
    sum = 0
    for i in range(middle, high): # We go up to high - 1
        sum += arr[i]
        if sum > right_max:
            right_max = sum
            right_index = i+1

    return (left_index, right_index, left_max + right_max)


def max_sub_array(arr, low, high):
    R'''
    This a recursive (divide and conquer) solution to the maximum subarray problem.
    O(nlogn) time. There is a linear solution at O(n) for this problem though.
    '''
    if low == high-1: # The array has one element
        return (low, high, arr[low])
    else:
        middle = (low + high) // 2
        left_low, left_high, left_sum = max_sub_array(arr, low, middle)
        right_low, right_high, right_sum = max_sub_array(arr, middle, high)
        middle_low, middle_high, middle_sum = max_middle_array(arr, low, middle, high)
        if (left_sum > right_sum) and (left_sum > middle_sum):
            return (left_low, left_high, left_sum)
        elif (right_sum > left_sum) and (right_sum > middle_sum):
            return (right_low, right_high, right_sum)
        else:
            return (middle_low, middle_high, middle_sum)



arr = [100, -113, 110, 85, -3560, 105, 102, 86, -63, 81, -2050, 101, 94, -50, 106, 101, -508, 79, 94, 90, 97]
l, h, s = max_sub_array(arr, 0, len(arr))
print(l, h, s)
print(arr[l:h])
