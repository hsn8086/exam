n = int(input())
a = list(map(int, input().split()))


max_l = 0
for d in range(1, n + 1):
    if n // d + 1 < max_l:
        break
    for dif in range(d):
        last = 0
        cnt = 0
        for j in range(dif, n, d):
            if last < a[j]:
                cnt += 1
            else:
                cnt = 1
            last = a[j]
            if cnt > max_l:
                max_l = cnt
print(max_l)
