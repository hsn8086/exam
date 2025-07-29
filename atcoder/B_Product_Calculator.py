n, k = map(int, input().split())
p = 1
for i in map(int, input().split()):
    p *= i
    if p >= 10 ** (k):
        p = 1
print(p)
