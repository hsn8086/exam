def solve(a, b):
    if a > b:
        return a
    res = a - (b - a)
    return res if res > 0 else 0


num_of_tc = int(input())
for _ in range(num_of_tc):
    a, b = map(int, input().split())
    print(solve(a, b))
