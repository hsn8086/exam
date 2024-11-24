import queue


def solve(num_of_op, ops):
    q = queue.LifoQueue()
    for op in ops:
        op_l = op.split()
        if op_l[0] == "push":
            q.put(int(op_l[1]))

        elif op_l[0] == "pop":
            if q.queue:
                q.get()
            else:
                yield "Empty"
        elif op_l[0] == "query":
            if q.queue:
                yield q.queue[-1]
            else:
                yield "Anguei!"
        elif op_l[0] == "size":
            yield len(q.queue)




num_of_ops = int(input())
ops = [input() for i in range(num_of_ops)]
for i in solve(num_of_ops, ops):
    print(i)
