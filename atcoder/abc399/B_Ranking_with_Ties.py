n = input()
a = []
for i, v in enumerate(input().split()):
    a.append([i, int(v), -1])
a.sort(key=lambda x: x[1], reverse=True)

for i in range(len(a)):
    a[i][2] = i + 1

for i in range(1, len(a)):
    if a[i][1] == a[i - 1][1]:
        a[i][2] = a[i - 1][2]

a.sort(key=lambda x: x[0])
print(*map(lambda x: x[2], a), sep="\n")
