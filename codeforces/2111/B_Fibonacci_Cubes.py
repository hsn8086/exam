fib = [0, 1, 2]
for i in range(10):
    fib.append(fib[-1] + fib[-2])

for _ in range(int(input())):
    ans = []
    n, m = map(int, input().split())
    for i in range(m):
        a, b, c = sorted(map(int, input().split()))
        if a >= fib[n] and b >= fib[n] and c >= fib[n] + fib[n - 1]:
            ans.append("1")
        else:
            ans.append("0")
    print("".join(ans))
