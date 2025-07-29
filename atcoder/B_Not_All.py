n, m = map(int, input().split())
s = set(range(1, m + 1))

a = map(int, input().split())

for i, v in enumerate(a):
    if v in s:
        s.remove(v)
    if not s:
        print(n - i)
        break
else:
    print(0)
