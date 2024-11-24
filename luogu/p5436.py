import math


def solve(n: int):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if math.gcd(i, j) == 1:
                if i * j > n:
                    return i * j
                else:
                    return n


num_of_tc = int(input())
for i in range(num_of_tc):
    print(solve(int(input())))
