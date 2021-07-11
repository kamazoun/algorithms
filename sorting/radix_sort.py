
R'''
O(mn + mk) n: size of the array, m number of digits in `longest` number, k the range of the current system (for decimal, k = 10)
Does not work on anything else but positive integer. This can be adjusted though by separating the negative and positive numbers or using abs().
To add float functionality, we can simply use a dict instead of a list.

'''
def radix_count_sort(arr, pos):
    values = 10 # The number of digits in decimal base
    freq = [0]*values
    output = [-1]*len(arr)

    for i in arr: # Calculate the frequency of the value (digit) at the current position (in the tens, the hundreds, ...)
        value = (i // pos) % values
        freq[value] += 1

    for i in range(1, values): # Adds up the frequencies, to correspond to index in the arr (two 0s and 2 1s would put 2 for the 0s and 4 for the 1s so we know the 1 occupy position 2 and 3 in the array)
        freq[i] += freq[i-1]

    for i in reversed(arr): # put each number from arr at its correspondent position in output according to its `final` digit (or rather the digit at the current position)
        value = (i // pos) % values
        output[freq[value] - 1] = i
        freq[value] -= 1

    return output


def radix_sort(arr):
    max = 0
    for i in arr: # Finds the max value in the arr in order to find out how many position we need to divide up to
        if i > max: max = i

    pos = 1
    while max >= 1:
        print(pos, arr)
        arr = radix_count_sort(arr, pos)
        pos *= 10
        max //= 10

    return arr



print(radix_sort([3, 5 , 8, 454 ,45, 89 ,68 , -8, -91, 5, 91]))

#t  = input()
