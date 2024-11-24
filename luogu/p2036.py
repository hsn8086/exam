from itertools import  combinations

def solve(n, a):
    ans = float('inf')
    
    for i in range(1, n + 1):
        for combo in combinations(a, i):

            total_sour = 1
            total_bitter = 0
            for s, b in combo:
                total_sour *= s
                total_bitter += b
            ans = min(ans, abs(total_sour - total_bitter))
    
    return ans


n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
print(solve(n, a))

