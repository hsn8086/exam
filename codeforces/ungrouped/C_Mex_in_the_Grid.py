from itertools import product
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))

def mex(lst):
    if not lst:
        return 0
    lst.sort()
    for i,v in enumerate(lst):
        if i!=v:
            return i
    return v+1
cnt=0
for l1,r1,l2,r2 in product(range(n+1),range(n+1),range(n+1),range(n+1)):
    toc=[]
    for lst in matrix[l1:r1]:
        toc.extend(lst[l2:r2])
    # if mex(toc):
    #     print(mex(toc),toc)
    cnt+=mex(toc)
print(cnt)
# import sys

# def main():
#     input = sys.stdin.read
#     data = input().split()
#     idx = 0
#     t = int(data[idx])
#     idx += 1
#     for _ in range(t):
#         n = int(data[idx])
#         idx += 1
#         positions = []
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 row_part = i * (n - i + 1)
#                 col_part = j * (n - j + 1)
#                 cover = row_part * col_part
#                 positions.append((-cover, i, j))  # Negative for descending sort
#         # Sort by cover (ascending because of negative), then by row, then by column
#         positions.sort()
#         # Create grid
#         grid = [[0]*n for _ in range(n)]
#         for num in range(n*n):
#             _, i, j = positions[num]
#             grid[i-1][j-1] = num
#         # Output
#         for row in grid:
#             print(' '.join(map(str, row)))

# if __name__ == '__main__':
#     main()
# from itertools import product
# from random import shuffle

# def clac_mtx(matrix,n):
#     def mex(lst):
#         if not lst:
#             return 0
#         lst.sort()
#         for i,v in enumerate(lst):
#             if i!=v:
#                 return i
#         return v+1
#     cnt=0
#     for l1,r1 in product(range(n+1),range(n+1)):
#         for l2,r2 in product(range(l1-2,n+1),range(r1-2,n+1)):
#             toc=[]
#             for lst in matrix[l1:r1]:
#                 toc.extend(lst[l2:r2])

#             cnt+=mex(toc)
#     return cnt

# lst=list(range(16))
# last=0
# for _ in range(100000000):
    
#     shuffle(lst)
#     matrix=[]
#     for i in range(4):
#         matrix.append(lst[i*4:(i+1)*4])
#     rst=clac_mtx(matrix,4)
#     if last<=rst:
#         last=rst
#         print(rst)
#         for l in matrix:
#             print(*l)
#         print()