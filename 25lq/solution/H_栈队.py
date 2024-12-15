from collections import deque

n, m, q = map(int, input().split())
stack = []
queue = deque()
elements = set()
for _ in range(q):
    cmd = input().split()
    op = int(cmd[0])
    if op == 1:
        x = int(cmd[1])
        if len(stack) < n:
            stack.append(x)
            elements.add(x)
    elif op == 2:
        x = int(cmd[1])
        if len(queue) < m:
            queue.append(x)
            elements.add(x)
    elif op == 3:
        if stack:
            temp = stack.pop()
            elements.discard(temp)
            if len(queue) < m:
                queue.append(temp)
                elements.add(temp)
    elif op == 4:
        if queue:
            temp = queue.popleft()
            elements.discard(temp)
            if len(stack) < n:
                stack.append(temp)
                elements.add(temp)
    elif op == 5:
        if stack:
            print(f"{stack[-1]}")
        else:
            print("SE")
    elif op == 6:
        if queue:
            print(f"{queue[0]}")
        else:
            print("QE")
    elif op == 7:
        x = int(cmd[1])
        if x in elements:
            print("YES")
        else:
            print("NO")
