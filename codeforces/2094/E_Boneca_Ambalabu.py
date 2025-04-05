def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        total = 0
        for num in a:
            total += num
        
        max_val = 0
        for x in a:
            curr = 0
            for y in a:
                curr += x ^ y
            max_val = max(max_val, curr)
        results.append(str(max_val))
    
    print("\n".join(results))
solve()