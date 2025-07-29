from math import ceil, floor


def cal(x):
    x -= 1
    if x<=0:
        return 0
    c = ceil(x / 2)
    f = floor(x / 2)
    return (c + 1) * c // 2 + (f + 1) * f // 2


for _ in range(int(input())):
    n, k = map(int, input().split())
    if k%2==1:
        print(0)
        continue
    k = k // 2
    l_ = n // k
    a = n % k
    b = k - a

    print(b * cal(l_) + a * cal(l_+1))
