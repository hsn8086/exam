import math


def solve(x, y, k):
    step = math.ceil(max(x, y) / k) * 2
    if x > y:
        step -= 1
    return step


num_of_tc = int(input())
for _ in range(num_of_tc):
    x, y, k = map(int, input().split())
    print(solve(x, y, k))
