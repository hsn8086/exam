import bisect

def solve(a,m):
    for i in m:
        idx = bisect.bisect_left(a, i)
        if a[idx] != i:
            yield -1
        else:
            yield (idx+1)
n, m = map(int, input().split())
a = list(map(int, input().split()))
m = map(int, input().split())

print(" ".join(map(str,solve(a,m))))