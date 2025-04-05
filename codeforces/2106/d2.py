import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = map(int, input[ptr:ptr+2])
        ptr +=2
        a = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        b = list(map(int, input[ptr:ptr+m]))
        ptr +=m
        
        # Compute prefix: prefix[p] is the maximum number of b's matched in a up to p (1-based)
        prefix = [0]*(m+2)
        i = 0
        j = 0
        while i < n and j < m:
            if a[i] >= b[j]:
                prefix[j+1] = prefix[j] +1
                j +=1
            i +=1
        if j >= m:
            print(0)
            continue
        
        # Compute suffix: suffix[p] is the number of b's matched from p to m (1-based)
        suffix = [0]*(m+2)
        i = n-1
        j = m-1
        while i >=0 and j >=0:
            if a[i] >= b[j]:
                suffix[j+1] = suffix[j+2] +1
                j -=1
            i -=1
        
        res = float('inf')
        # Check for each possible p (1-based) in b
        for p in range(1, m+1):
            # The first p-1 can be matched in a, and the remaining m-p can be matched after
            if prefix[p-1] >= p-1 and suffix[p+1] >= (m - p):
                res = min(res, b[p-1])
        
        if res != float('inf'):
            print(res)
        else:
            print(-1)

solve()