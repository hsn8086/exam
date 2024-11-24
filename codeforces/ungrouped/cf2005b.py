import bisect


def solve(teachers_cn: list[int], david_cn: int, num_of_cell: int):
    idx = bisect.bisect(teachers_cn, david_cn)
    if idx == 0:
        return teachers_cn[0] - 1
    elif idx == len(teachers_cn):
        return num_of_cell - teachers_cn[-1]
    else:
        left = teachers_cn[idx - 1]
        right = teachers_cn[idx]
        return (right - left) // 2


def inp_flow():
    num_of_tc = int(input())
    for i in range(num_of_tc):
        num_of_cell, num_of_teacher, num_of_query = map(int, input().split())
        teachers_cn = list(map(int, input().split()))
        teachers_cn.sort()
        david_cns = list(map(int, input().split()))
        for david_cn in david_cns:
            yield solve(teachers_cn, david_cn, num_of_cell)


for i in inp_flow():
    print(i)


"""
1
16 3 12
3 7 12
1 2 4 5 6 8 9 10 11 13 14 15
"""
