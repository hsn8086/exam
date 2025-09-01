n, m = map(int, input().split())
matrix_a = [map(int, input().split()) for _ in range(n)]
matrix_b = [map(int, input().split()) for _ in range(n)]

for a_lst, b_lst in zip(matrix_a, matrix_b):
    print(*(str(a + b) for a, b in zip(a_lst, b_lst)))
