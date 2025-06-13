from collections import defaultdict


def event_loop(s):
    stk, last_rst = [s], None
    while stk:
        try:
            func, last_rst = stk[-1].send(last_rst), None
            stk.append(func)
        except StopIteration as e:
            last_rst = e.value
            stk.pop()
    return last_rst


def clac(a: list, p: int, e: dict):
    if len(e[p]) == 0:
        return a[p - 1]

    m = float("+inf")
    for i in e[p]:
        v = yield clac(a, i, e)
        m = min(v, m)
    if m < a[p - 1]:
        return m

    v = (a[p - 1] + m) // 2
    a[p - 1] = v
    return v


for _ in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    fat = list(map(int, input().split()))

    e = defaultdict(list)
    for i, f in enumerate(fat):
        e[f].append(i + 2)
    # print(a)
    m = float("inf")
    for i in e[1]:
        m = min(event_loop(clac(a, i, e)), m)
    # print(a)
    # print(e)
    print(m + a[0])
