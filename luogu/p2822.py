ntc, k = map(int, input().split())
nod = 10
matrix = [[0 for _ in range(nod + 10)] for _ in range(nod + 10)]
cm = [[0 for _ in range(nod + 5)] for _ in range(nod + 5)]

for i in range(nod):
    cm[i][0] = 1
for n in range(1, nod):
    for m in range(1, nod):
        cm[m][n] = (cm[m - 1][n - 1] + cm[m - 1][n]) % k

for n in range(1, nod):
    for m in range(1, nod):
        matrix[n][m] = matrix[n - 1][m] + matrix[n][m - 1] - matrix[n - 1][m - 1]
        if cm[m][n] == 0:
            matrix[n][m] += 1
import pprint

pprint.pp(matrix)
for _ in range(ntc):
    n, m = map(int, input().split())
    print(matrix[n][m])
