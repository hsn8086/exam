from collections import deque, defaultdict

deqs = defaultdict(deque)
for _ in range(int(input())):
    cmd, a_r, *args_r = input().split()
    args = map(int, args_r)
    a = int(a_r)
    deq = deqs[a]
    if cmd == "pop_back":
        if deq:
            deq.pop()
    elif cmd == "pop_front":
        if deq:
            deq.popleft()
    elif cmd == "push_back":
        deq.append(*args)
    elif cmd == "push_front":
        deq.appendleft(*args)
    elif cmd == "size":
        print(len(deq))
    elif cmd == "front":
        print(deq[0])
    elif cmd == "back":
        print(deq[-1])
