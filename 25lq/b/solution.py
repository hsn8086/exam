import heapq

n, m = map(int, input().split())
a = [int(x) for x in input().split()]

q = []
for i in range(n):
    if len(q) < m:
        heapq.heappush(q, a[i])
    else:
        heapq.heappushpop(q, a[i])

while q:
    print(heapq.heappop(q), end=" ")
