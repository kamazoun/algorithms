"""
You are given a number as a string num and an integer k. Build the largest possible number using digits of num such that the no digits appear more than k times consecutively. You can use all or some digits in num.
"""

def largest_possible_number(num, k):
    numbers = list(num)
    numbers.sort(reverse=True)

    results = []
    i = k
    while numbers:
        if not results:
            results.append(numbers.pop(0))
            i -= 1
            continue
        if results[-1] != numbers[0]:
            results.append(numbers.pop(0))
            i = k - 1
            continue
        if i > 0:
            results.append(numbers.pop(0))
            i -= 1
        else:
            t = numbers[:]
            indexToPop = 0
            while t and t[0] == results[-1]:
                t.pop(0)
                indexToPop += 1
            # print(indexToPop, len(numbers))
            if indexToPop >= len(numbers): # There are no more different digits in the stack. Will not be able to use the whole length of num
                # print('INDEX OUT OF BOUNDS')
                # print(t, indexToPop, numbers)
                break
            print(t, indexToPop, numbers[indexToPop])
            print(numbers)
            results.append(numbers.pop(indexToPop))
            print(results)
            print(numbers)
            # i = k - 1 NOT NEEDED
        
        # if not results or results[-1] != n or 0 < i:
        
        
    return ''.join(results)
 

print(largest_possible_number('3391933', 3))
print(largest_possible_number('1121212', 2))
print(largest_possible_number('5416489688676561687', 2))
print(largest_possible_number('5416489688676561687', 1))
print(largest_possible_number('5416489688676561687', 5))