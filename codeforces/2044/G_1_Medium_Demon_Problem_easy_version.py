for _ in range(int(input())):
    n = int(input())
    r = [int(x) - 1 for x in input().split()]

    curr = frozenset(range(n))
    seen = {curr}
    year = 1

    while True:
        curr = frozenset(r[i] for i in curr)
        if curr in seen:
            print(year + 1)
            break

        seen.add(curr)
        year += 1
