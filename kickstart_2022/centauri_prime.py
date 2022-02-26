from sys import stdin

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def solution(kingdom : str) -> str:
    if kingdom[-1].lower() == 'y':
        return 'nobody'
    elif kingdom[-1] in vowels:
        return 'Alice'
    else:
        return 'Bob'

if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        k = stdin.readline().strip()
        r = solution(k)
        print(f'Case #{i + 1}: {k} is ruled by {r}.')
