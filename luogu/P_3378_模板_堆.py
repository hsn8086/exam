import heapq

heap = []
for _ in range(int(input())):
    cmd = tuple(map(int, input().split()))
    if cmd[0] == 1:
        heapq.heappush(heap, cmd[1])
    elif cmd[0] == 2:
        print(heap[0])
    elif cmd[0] == 3:
        heapq.heappop(heap)
