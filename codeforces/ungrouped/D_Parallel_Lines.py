from collections import defaultdict
from fractions import Fraction


def get_k(x1, y1, x2, y2):
    x, y = x1 - x2, y1 - y2
    return Fraction(x, y)


def check(lst, k: Fraction):
    groups = []
    while lst:
        sub = []
        i, data = lst.pop()
        x, y = data
        sub.append(i + 1)
        to_del = []
        for i, data in enumerate(lst):
            j, d2 = data
            x2, y2 = d2
            if y == y2:
                continue
            if k == get_k(x, y, x2, y2):
                to_del.append(i)
                sub.append(j + 1)

        if len(sub) == 0:
            return -1
        to_del.reverse()
        for i in to_del:
            lst.pop(i)
        groups.append(sub)
    return groups


n, k_cnt = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]

for i, data in enumerate(lst):
    x, y = data

    for x2, y2 in lst[i + 1 :]:
        if y2 != y:
            k = get_k(x, y, x2, y2)

            # match
            cp_lst = list(enumerate(lst))
            groups = check(cp_lst, k)
            if len(groups) == k_cnt:
                for sub in groups:
                    print(len(sub), *sub)
                break
        else:
            ymp = defaultdict(list)

            for i, data in enumerate(lst, 1):
                x2, y2 = data
                ymp[y2].append(i)

            if len(ymp) == k_cnt:
                for lst in ymp.values():
                    print(len(lst), *lst)
                break
    else:
        continue
    break
