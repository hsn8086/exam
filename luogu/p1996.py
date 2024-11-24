def solve(n, m):
    lst = [i for i in range(1, n + 1)]
    offset = -1
    while lst:
        yield str(lst.pop(offset + m))
        offset += m - 1
        while offset + m >= len(lst) and len(lst):
            offset -= len(lst)


n, m = map(int, input().split())
print(" ".join(solve(n, m)))
