n, q = map(int, input().split())
diff = [False] * (n + 10)

for _ in range(q):
    li, ri = map(int, input().split())
    diff[li - 1] = not diff[li - 1]
    diff[ri] = not diff[ri]

now = 0
for i in range(n):
    if diff[i]:
        now = 1 if now == 0 else 0
    print(now, end="")
print("\n")
