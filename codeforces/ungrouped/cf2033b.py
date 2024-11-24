# def solve():
#     t = int(input())  # Number of test cases
#     for _ in range(t):
#         n = int(input())  # Size of matrix
#         a = [list(map(int, input().split())) for _ in range(n)]

#         operations = 0

#         # Traverse diagonals starting from the top left corner
#         for start_row in range(n):
#             i, j = start_row, 0
#             while i < n and j < n:
#                 # Count how many increments are needed for this element to become non-negative
#                 if a[i][j] < 0:
#                     operations += abs(a[i][j])
#                 i += 1
#                 j += 1

#         print(operations)

# def solve():
#     t = int(input())  # number of test cases
#     for _ in range(t):
#         n = int(input())  # matrix size
#         matrix = [list(map(int, input().split())) for _ in range(n)]

#         operations = 0

#         # Traverse through all possible diagonals
#         for d in range(n):  # d is the length of the diagonal
#             for i in range(n - d):
#                 j = i + d
#                 # If any diagonal element is negative, we need to increase it
#                 if matrix[i][j] < 0:
#                     # The number of operations needed to make the diagonal element non-negative
#                     operations += abs(matrix[i][j])
#                     # Update the matrix
#                     for k in range(d + 1):
#                         matrix[i + k][j - k] += abs(matrix[i][j])

#         print(operations)

# # Read input
# solve()


def solve(n, m):
    for offset in range(-n + 1, n):
        lst = []
        for j in range(n):
            if 0 <= j + offset < n:
                lst.append(m[j][j + offset])
        yield min(lst)


num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())
    m = [[*map(int, input().split())] for _ in range(n)]
    res = sum(filter(lambda e: e <= 0, solve(n, m)))
    print(-res)
