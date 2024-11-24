import queue

n = int(input())
q = queue.Queue()
for _ in range(n):
    op = input().split()
    if op[0] == "1":
        q.put(op[1])
    elif op[0] == "2":
        if q.queue:
            q.get()
        else:
            print("ERR_CANNOT_POP")
    elif op[0] == "3":
        if q.queue:
            print(q.queue[0])
        else:
            print("ERR_CANNOT_QUERY")
    elif op[0] == "4":
        print(len(q.queue))
