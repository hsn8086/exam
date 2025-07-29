from collections import defaultdict

n = int(input())
cnt_d = defaultdict(int)
lst = set()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j <= n:
            cnt_d[i * j] += 1
            lst.add(i * j)

        else:
            break
print(list(filter(lambda x: x[1] > 1, cnt_d.items())))
cnt = 0
for i in lst:
    for j in lst:
        if j + i <= n:
            cnt += cnt_d[j] * cnt_d[i]

print(cnt)
