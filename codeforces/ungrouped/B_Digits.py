from math import factorial

lst = [
    [],
    [1],
    [1],
    [1, 3],  # 111
    [1],
    [1],
    [1, 3, 7],
    [1],
    [1],
    [1, 3, 9],
]

for _ in range(int(input())):
    n, d = map(int, input().split())
    s = set()
    for i in range(1, d + 1):
        if d % i == 0 and i % 2 == 1:
            s.add(i)
    if n > 7:
        for i in lst:
            s.update(i)
    else:
        nf = factorial(n)
        for i in range(1, 10):
            if nf % i == 0:
                s.update(lst[i])
    print(*sorted(s))
