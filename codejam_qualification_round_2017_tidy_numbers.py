def tidy(n : str) -> str:
    s = [int(i) for i in n]
    n = len(s)
    prev = s[-1]
    for i in reversed(range(n)):
        if prev < s[i]:
            s[i] -= 1
            s[i+1:] = [9] * (n - i - 1)
        prev = s[i]

    return ''.join(str(i) for i in s).lstrip('0')


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = input()
        r = tidy(n)
        print(f'Case #{i+1}: {r}')
