def solve(x: int, a: list[int]):
    tm = {}
    a.sort()
    last = -1
    for i in a:
        if i == last:
            tm[i % x] = tm.get(i % x, 0) + 1

        elif i == last + 1:
            pass
        else:
            for j in range(last + 1, i):
                if j % x in tm:
                    tm[j % x] -= 1
                    if not tm[j % x]:
                        tm.pop(j % x)
                else:
                    return j
        last = i

    while tm:
        last += 1
        if last % x in tm:
            tm[last % x] -= 1
            if not tm[last % x]:
                tm.pop(last % x)
        else:
            last -= 1
            break
    return last + 1


num_of_tc = int(input())
for _ in range(num_of_tc):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(x, a))
