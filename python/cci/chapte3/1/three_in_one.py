"""
Three in One: Describe how you could use a single array to implement three stacks.
"""

"""
1. we could put elements of the ith stack in the indexes i % 3 == i - 1. So the first element of the first stack would be at index 0, the first element of the second stack would be at index 1, and the first element of the third stack would be at index 2. Then it would be easy to find the top of each stack by looking at the last element in the array that is at index i % 3 == i - 1. But it will not be efficient to push elements into any stack (particularly if they end up being of different length).

2. we could put elements of the first stack in the first third of the array, the second stack in the second third of the array, and the third stack in the last third of the array. This would be a simple implementation, but it would not be very efficient because we would have to keep track of the size of each stack and make sure that they don't overflow.

3. (with author's hint) we could assign different indexes to each stack. For instance the first stack, would only use even numbers, the second only odds but not prime and the third only prime numbers. The stacks would be of different sizes. By considering the array to be circular, we could implement it to avoid overflow (by clycling through and replacing the top of the overflowing stack). By keeping track of the starting index of each stack, we could implement pop() and push() operations in O(1).
"""