import math

n = int(input())
a = list(map(int, input().split()))

lst = [1] * n
for i in range(1, n):
    sum_ = 0
    for j in range(0, i):
        if math.gcd(a[i], a[j]) != 1:
            sum_ += lst[j]
    lst[i] = sum_

print(lst[-1])
