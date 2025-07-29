def mex(lst):
    lst = sorted(set(lst))
    m = lst[0] - 1
    for i in lst:
        if i - 1 == m:
            m = i
        else:
            return m + 1
    return m + 1


for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        print(s + chr(mex([ord("a"), ord(s)])))
        continue
    idx = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            idx = i
            break

    print(
        s[: idx + 1]
        + chr(mex(list(map(ord, s[idx : idx + 2])) + [ord("a")]))
        + s[idx + 1 :]
    )
