from random import randint

rnd = randint(100, 1000)
for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    last_sp = set([next(a) + rnd])
    sp = set()
    cnt = 1
    for i in a:
        sp.add(i + rnd)
        if i + rnd in last_sp:
            last_sp.remove(i + rnd)
            if not last_sp:
                last_sp = sp
                sp = set()
                cnt += 1

    print(cnt)
