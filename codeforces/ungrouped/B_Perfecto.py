sq = {i**2 for i in range(353554)}
for _ in range(int(input())):
    n = int(input())
    if (1 + n) * n // 2 in sq:
        print(-1)
        continue
    sum_ = 0
    rst = list(range(1, n + 1))
    for i, v in enumerate(rst):
        sum_ += v
        if sum_ in sq:
            sum_ += 1

            rst[i], rst[i + 1] = rst[i + 1], rst[i]
    print(*rst)
