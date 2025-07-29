from collections import defaultdict, deque


n, m = map(int, input().split())
e = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

for i, lst in e.items():
    if len(lst) != 2:
        print("No")
        break
else:
    if 1 not in e:
        print("No")
    else:
        ptrq = deque()
        ptrq.append(1)
        while ptrq:
            now = ptrq.popleft()
            if now not in e:
                continue
            nxt = e[now]
            ptrq.extend(nxt)
            e.pop(now)

        if e:
            print("No")
        else:
            print("Yes")
