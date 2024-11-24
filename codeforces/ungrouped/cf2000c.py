def solve(n: int, a: list[int], m: int, sl: list[str]):
    length = len(a)
    for s in sl:
        d = {}
        used = set()
        if len(s) != length:
            yield "No"
            continue
        for i, v in enumerate(s):
            if v not in d:
                d[v] = a[i]
                if a[i] in used:
                    yield "No"
                    break
                else:
                    used.add(a[i])
            if d[v] != a[i]:
                yield "No"
                break
        else:
            yield "Yes"


num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    s = (input() for _ in range(m))
    for i in solve(n, a, m, s):
        print(i)
