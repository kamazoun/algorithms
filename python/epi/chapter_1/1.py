

def count_bits(x: int) -> int:
    if not x:
        return 0
    count = 0
    while x:
        if x & 1:
            count += 1
        x >>= 1
    return count

print(count_bits(3))