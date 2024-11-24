# def solve(n, a):
#     lst = sorted(a, key=lambda an: an[0], reverse=True)
#     while lst:
#         min_idx = 0
#         for i in range(len(lst)):
#             if lst[min_idx][1] > lst[i][1]:
#                 min_idx = i
#         p1 = lst.pop(min_idx)
#         yield from p1
#         last = p1[1]
#         while lst:
#             if lst[-1][0] > last:
#                 p1 = lst.pop(-1)
#                 yield from p1
#                 last = p1[1]
#             else:
#                 break


def solve(n, a):
    lst = sorted(a, key=lambda an: an[1], reverse=True)
    while lst:
        p = lst.pop(-1)
        yield from p
        while lst:
            for _i in range(len(lst)):
                i = len(lst) - _i - 1
                if lst[i][0] > p[1]:
                    p = lst.pop(i)
                    yield from p
                    break
            else:
                p = None
                break
            if p is None:
                break


# def solve(n, a):
#     for i in sorted(a, key=lambda an: an[0]):
#         yield from i


num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())
    a = (tuple(map(int, input().split())) for _ in range(n))
    print(" ".join(map(str, solve(n, a))))
