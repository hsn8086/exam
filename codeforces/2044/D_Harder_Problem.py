from itertools import chain, pairwise


def dedup_sort(a):
    lst = sorted(enumerate(a), key=lambda x: x[1])  # 按值排序

    sorted_lst = [lst[0]]
    for e in lst[1:]:  # 去重
        if sorted_lst[-1][1] != e[1]:
            sorted_lst.append(e)

    ordered_lst = sorted(sorted_lst, key=lambda x: x[0])  # 按插入顺序排序
    return map(lambda x: x[1], sorted_lst), map(lambda x: x[1], ordered_lst)  # 输出


for _ in range(int(input())):  # 处理多tc
    n = int(input())
    sorted_a, ordered_a = dedup_sort(map(int, input().split()))

    print(
        *ordered_a,  # 输出ordered数组
        *chain.from_iterable(  # 输出间隙
            map(
                lambda t: range(t[0] + 1, t[1]), pairwise(chain([0], sorted_a, [n + 1]))
            )
        ),
    )
