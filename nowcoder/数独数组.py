from collections import Counter

n = int(input())
a = map(int, input().split())
c = Counter(a)
for i in range(1, 10):
    if c[i] not in [n // 9, n // 9 + 1]:
        print("NO")
        break
else:
    print("YES")
