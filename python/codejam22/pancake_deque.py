from sys import stdin

if __name__ == '__main__':
    t = int(stdin.readline())

    for case in range(t):
        n = int(stdin.readline())
        ds = list(map(lambda x: int(x), stdin.readline().split()))
    
        i, j = 0, len(ds) - 1
        current = 0
        maxi = 0
        while i != j:
            if ds[i] < ds[j]:
                if ds[i] >= current:
                    current = ds[i]
                    maxi += 1
                i += 1
            else:
                if ds[j] >= current:
                    current = ds[j]
                    maxi += 1
                j -= 1
            
        print(f'Case #{case + 1}: {maxi}')
