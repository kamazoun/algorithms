if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        l = input().split()
        m = input().split()
        n = input().split()
        
        r = [0, 0, 0, 0]
        total = 0
        for z in range(4):
            r[z] = min(min(int(l[z]), int(m[z])), int(n[z]))
            total += r[z]
            
            if total >= 10**6:
                break
        
        if total > 10**6:
            d = total - 10**6
            for ind in range(4):
                if r[ind] >= d:
                    r[ind] -= d
                    total -= d
                    #d = 0
                    break
                else:
                    d -= r[ind]
                    total -= r[ind]
                    r[ind] = 0
                    
        if total != 10**6: print(f'Case #{i+1}: IMPOSSIBLE')   
        else:
            line = ' '.join(str(i) for i in r)
            print(f'Case #{i+1}: {line}')
            
    
