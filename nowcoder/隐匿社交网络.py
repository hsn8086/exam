for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    networks = []

    for w in a:
        lst = []
        for i, nw in enumerate(networks):
            v, c = nw
            if w & v >= 1:
                lst.append(i)

        if len(lst) == 1:
            networks[lst[0]][0] |= w
            networks[lst[0]][1] += 1
        elif len(lst) >= 2:
            merge = []
            for i, i_ in enumerate(lst):
                merge.append(networks.pop(i_ - i))

            rst = [0, 0]
            for v, c in merge:
                rst[0] |= v
                rst[1] += c

            rst[0] |= w
            rst[1] += 1

            networks.append(rst)
        else:
            networks.append([w, 1])
    print(max(map(lambda t: t[1], networks)))
