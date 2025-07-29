import math


def transf(matrix):
        # for lst in zip(*matrix):
        #     print( *lst[::-1])
        # print( )
    return [lst[::-1] for lst in zip(*matrix)]


def cmp(m1, m2):
    cnt = 0
    for l1, l2 in zip(m1, m2):
        for i1, i2 in zip(l1, l2):
            if i1 != i2:
                cnt += 1

    return cnt


n = int(input())
matrix1 = []
matrix2 = []
for _ in range(n):
    matrix1.append(list(input()))
for _ in range(n):
    matrix2.append(list(input()))

cnt = float("inf")

for i in range(4):
    matrix1 = transf(matrix1)
    cnt = min(cnt, cmp(matrix1, matrix2) + (i+1)%4)
print(cnt)
