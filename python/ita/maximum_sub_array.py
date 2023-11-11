R'''
Suppose that you been offered the opportunity to invest in the Volatile Chemical Corporation. Like the chemicals the company produces, the stock price of the Volatile Chemical Corporation is rather volatile. You are allowed to buy one unit of stock only one time and then sell it at a later date, buying and selling after the close of trading for the day. To compensate for this restriction, you are allowed to learn what the price of the stock will be in the future. Your goal is to maximize your profit.
'''


def max_middle_array(arr, low, middle, high): # procedure for next function
    R'''
    The goal is to find the maximum subarray that spans around `middle`, i.e from low <= middle < high.
    The technique is to find the maximum to the left of middle and the maximum to the right of middle then combine them.
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
    Author's
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


#TODO: It does not work on all cases
def max_sub_array_linear(arr, low, high):
    R'''
    Mine
    Use the following ideas to develop a nonrecursive, linear-time algorithm for the maximum-subarray problem. Start at the left end of the array, and progress toward the right, keeping track of the maximum subarray seen so far. Knowing a maximum subarray of A[1 : j] , extend the answer to find a maximum subarray ending at index j + 1 by using the following observation: a maximum subarray of A[1 : j + 1] is either a maximum subarray of A[1 : j]  or a subarray A[i : j + 1], for some 1 <= i <= j + 1. Determine a maximum subarray of the form A[i : j + 1] in constant time based on knowing a maximum subarray ending at index j .

    This will be a linear solution at O(n) for this problem.
    '''
    if low == high - 1:
        return (low, high, arr[low])

    d = [-1] * len(arr)
    d[0] = arr[0]
    l = 0
    h = 1
    t_h = 0
    t_l = 0

    for j in range(1, len(arr)):
        if d[j] != -1:
            continue
            #return d[j]
        else:
            if (arr[j] > 0) and (h == j):
                d[j] = d[j - 1] + arr[j]
                h = j + 1
                #return d[j]
            else: # The max is either d[j-1] or is somewhere between h and j
                s = 0
                max_sum = float('-inf')

                #print(h, j)
                for i in range(h, j):
                    if s < 0 and (arr[i] > 0):
                        s = 0
                        t_h = i+1
                        t_l = i
                    s += arr[i]
                    if s >= max_sum:
                        max_sum = s
                        t_h = i+1
                        t_l = i
                #print(d[j-1], max_sum)

                if (max_sum >= d[j-1]): #and (t_h > t_l):
                    d[j] = max_sum
                    h = t_h
                    l = t_l
                    #print(s, max_sum, t_l, t_h)
                else:
                    d[j] = d[j-1]


    #print(d)
    return (l, h, d[-1])


#def find_max_sub_array(): From epi 13.py gives another beautiful solution


arr = [100, 50, 25, 85, -3560, -3, 105, 102, 86, -63, 81, -2050, 101, 94, -50, 106, 101, -508, 79, 94, 90, 97]
l, h, s = max_sub_array(arr, 0, len(arr))
print(l, h, s)
print(arr[l:h])

l,h,s = max_sub_array_linear(arr, 0, len(arr))
print(l, h, s)
print(arr[l:h])
