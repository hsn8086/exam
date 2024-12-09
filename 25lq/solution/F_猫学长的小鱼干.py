n, m = map(int, input().split())
a: list[int] = list(map(int, input().split()))
a.sort()
print(" ".join(map(str, a[n - m :])))
