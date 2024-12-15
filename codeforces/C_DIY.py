from collections import Counter

ntc = int(input())
for _ in range(ntc):
    n = int(input())
    a = Counter(map(int, input().split()))
    b = []
    for v, c in a.items():
        b.extend([v] * (c // 2))
    if len(b) < 4:
        print("NO")
        continue
    b.sort()
    print("YES")
    print(b[0], b[1], b[0], b[-1], b[-2], b[1], b[-2], b[-1])
