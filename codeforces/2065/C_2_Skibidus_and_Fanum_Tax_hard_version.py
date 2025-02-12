import bisect

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = map(int, input().split())
    b = list(map(int, input().split()))
    b.sort()

    last = float("-inf")
    for e in a:
        idx = bisect.bisect(b, e + last)
        idx = max(idx - 3, 0)
        if idx == len(b):
            idx -= 1
        while b[idx] - e < last:
            idx += 1
            if idx >= len(b):
                idx -= 1
                break
        max_an = max(b[idx] - e, e)
        min_an = min(b[idx] - e, e)
        if min_an >= last:
            last = min_an
        elif max_an >= last:
            last = max_an
        else:
            print("NO")
            break

    else:
        print("YES")
    """
    """