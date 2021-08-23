


def sieve_simple(n):
    numbers = [i for i in range(2, n+1)]

    for i in numbers:
        c = i+i
        while c <= n:
            if c in numbers: numbers.remove(c)
            c += i

    primes = [i for i in numbers if i != 0]
    return primes


def sieve(n):
    R'''
    We can still optimize this by checking from prime * prime
    Also we can init the array with only odd numbers as even numbers from 2 are not primes
    '''
    numbers = [False] * 2 + [True] * (n-1)

    for i in range(2, n+1):
        c = i+i
        while c <= n:
            numbers[c] = False
            c += i

    primes = [i for i in range(2, n+1) if numbers[i]]
    return primes

def sieve_odd(n):
    R'''
    We will attempt to reduce the size by only storing odd numbers
    '''
    arr = [True] * (n//2) # arr[0] represents `2` and will be the only even number in the arr, other index will represent 2*index+1

    i = 1
    while i < len(arr):
        if arr[i]: # TODO: Here we can find a way to start from an index higher than i.
            val = 2 * i + 1
            k = i + val
            t = 2
            while k < n // 2:
                arr[k] = False
                k = i + val * t
                t += 1
        i += 1

    primes = [2] + [2*i+1 for i in range(1, len(arr)) if arr[i]]
    return primes

a = sieve_odd(100)
print(a)
