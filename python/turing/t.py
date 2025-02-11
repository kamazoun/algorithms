"""
given an int n return all pairs  of primes that add to n
"""




def s(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    results = []
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            results.append((i, n - i))
    return sorted(results)