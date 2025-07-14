matrix = []

for _ in range(v := int(input())):
    matrix.append(bytearray(map(int, input().split())))


for k in range(v):
    for i in range(v):
        for j in range(v):
            matrix[i][j] = matrix[i][j] | (matrix[i][k] & matrix[k][j])


for line in matrix:
    print(*line)
