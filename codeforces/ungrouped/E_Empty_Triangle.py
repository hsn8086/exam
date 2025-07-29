
import random

import sys
def output(s):
    sys.stdout.write(s + "\n")
    sys.stdout.flush()


def answer(*args):
    output("! " + " ".join(map(str, args)))


def query(*args):
    output("? " + " ".join(map(str, args)))
    return input()


def solve(n):
    if n == 3:
        answer(1, 2, 3)
        return

    rst = random.sample(range(1, n + 1), k=3)
    while True:
        rt = int(query(*rst))
        if rt == 0:
            answer(*rst)
            return
        if rt == -1:
            ...
        rst.pop(random.randint(0, 2))
        rst.append(rt)


for _ in range(int(input())):
    n = int(input())
    solve(n)
