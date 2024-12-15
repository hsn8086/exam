n, p = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
a = set(filter(lambda t: t[1], a))

print(len(a))
