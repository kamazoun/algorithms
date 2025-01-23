def longest_alternating_subsequence(arr):
    if not arr:
        return []

    las = [arr[0]]  # Initialize the longest alternating subsequence with the first element

    for i in range(1, len(arr)):
        if arr[i] != las[-1]:  # Check if current element is different from the last added element
            las.append(arr[i])

    return len(las) # COULD USE A NUMBER INSTEAD OF ARRAY

# Example usage:
arr = [1, 0, 1, 1, 0, 1, 0, 0, 1]
result = longest_alternating_subsequence(arr)
print("Longest alternating subsequence:", result)