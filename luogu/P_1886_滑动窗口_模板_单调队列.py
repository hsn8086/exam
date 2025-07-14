from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
sil_min = deque()
sil_max = deque()
ans_min = []
ans_max = []
for i, v in enumerate(a):
    while sil_min and v < sil_min[-1][1]:
        sil_min.pop()
    while sil_max and v > sil_max[-1][1]:
        sil_max.pop()
    sil_min.append((i, v))
    sil_max.append((i, v))
    while sil_min and i - sil_min[0][0] >= k:
        sil_min.popleft()
    while sil_max and i - sil_max[0][0] >= k:
        sil_max.popleft()
    if i >= k - 1:
        ans_min.append(sil_min[0][1])
        ans_max.append(sil_max[0][1])

print(*ans_min)
print(*ans_max)
