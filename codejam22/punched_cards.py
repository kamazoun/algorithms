def s(r: int, c: int)->list:
    # edge case non existant due to constraints
    result = []
    for i in range(2*r + 1):
        line = []
        for j in range(2*c + 1):
            if i < 2 and j < 2:
                line.append('.')
                continue
            if i % 2 == 0: #is_plus_line:
                if j  % 2 == 0: line.append('+')
                else: line.append('-')
            else:
                if j % 2 == 0: line.append('|')
                else: line.append('.')
        v = ''.join(i for i in line)
        result.append(v)
    return result
            


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m, n = input().split()
        r, c = int(m),  int(n)
        y = s(r, c)
        print(f'Case #{i+1}:')
        for l in y:
            print(l)
            
