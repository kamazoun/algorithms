
"""
You're embarking on a construction project, aiming to create a wooden fence using discarded wood pieces.
Your plan is to utilize these pieces as the planks that make up your fence. An intrinsic rule that you must follow is that every plank in your fence must be the same length.
There is a possibility that you have two smaller pieces of wood whose total length equals the required plank length. In this scenario, you can bind them together to birth a fully-grown plank.
Yet, one must remember that the permit only allows fusing two pieces of wood together to form a plank, as adding a third would compromise the fence's strength. Also, there are restrictions on the tools, allowing you only a hammer and nails; this denies you the opportunity to reduce the sizes of the wood pieces (since you don't have access to a saw).
Coming to your arsenal, you have an array named 'wood' at your disposal. Each entry in this array represents the length of the individual wood pieces you have in your possession.
Setting foot on this journey, your objective is to maximize the length of the fence you construct, i.e., to have as many planks on your fence as possible. You have the freedom to determine the length of the planks, and subsequently, the height of the fence. Moreover, you have the liberty to choose how you can assemble the pieces of wood from your collection.
Inquire yourself, what's the maximum number of planks that you can incorporate into your wooden fence? This indeed is the answer you seek.
Example 1:
Input: [22, 12, 13, 22, 22, 22, 14, 22, 17, 22]
Output: 6
Example 2:
Input: [8, 13, 7, 13, 5, 13, 4, 13, 6, 13]
Output: 7
Explanation: You can use 5 planks of 13 length. Then 2 planks can be combined 8+5=13 and 2 other planks 7+6=13. Which will give you 7 planks in total.
Constraints:
 * 1 <= wood <= 200
 * 1 <= wood[i] <= 10^9
"""


from collections import Counter

def solution(wood):
    """
    Calculates the maximum number of planks that can be constructed from the given wood pieces.

    Args:
        wood: A list of integers representing the lengths of the wood pieces.

    Returns:
        The maximum number of planks that can be constructed.
    """

    all_lengths = Counter(wood)

    all_results = {}
    for length, count in all_lengths.items():
        all_results[length] = count

    seen = []

    for key, value in all_lengths.items():
        for key2, value2 in all_lengths.items():
            if (key2, key) in seen:
                continue
            seen.append((key, key2))
            if key == key2:
                continue
                if key in all_results:
                    all_results[key] += value
                else:
                    all_results[key] = value
            else:
                if (key + key2) in all_results:
                    all_results[(key + key2)] += min(value, value2)
                else:
                    all_results[(key + key2)] = min(value, value2)
    print(all_results)
    return max(all_results.values())


# Example usage
wood1 = [22, 12, 13, 22, 22, 22, 14, 22, 17, 22]
wood2 = [8, 13, 7, 13, 5, 13, 4, 13, 6, 13]

print(f"Example 1: Max planks = {solution(wood1)}")  # Output: 6
print(f"Example 2: Max planks = {solution(wood2)}")  # Output: 7