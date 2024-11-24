def solve(n: int, a: list[int]):
    if n <= 2:
        return -1
    a.sort()
    rt = a[n // 2] * 2 * n - sum(a) + 1
    return rt if rt > 0 else 0


num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())
    a = map(int, input().split())
    print(solve(n, list(a)))
