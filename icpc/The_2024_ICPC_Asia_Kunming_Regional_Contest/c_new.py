
import math
def calc0(u):
        v = min(n, ((u + k - 1) // k) * k)
        up = (u - 1) // k + 1
        u += (v - u) // up * up
        return u

def calc1(u):
    v = 0
    while ((u + k - 1) // k) > ((v + k - 1) // k):
        tmp = ((u + k - 1) // k) - ((v + k - 1) // k)
        v = u
        u += tmp
    return u

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())

   
    u = 1
    while True:
        v = calc0(u)
        if v <= n:
            u = v
        v = calc1(u)
        if v > n:
            break
        u = v
    print(u)