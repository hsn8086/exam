ntc=int(input())
for _ in range(ntc):
    n = input()
    s = sum(int(d) for d in n) % 9
    cnt_2 = n.count('2')
    cnt_3 = n.count('3')
    t = (-s) % 9
    possible = False
    for x in range(min(cnt_2, 8) + 1):
        two_mod = (2 * x) % 9
        for y in range(min(cnt_3, 2) + 1):
            delta = (two_mod + (6 * y) % 9) % 9
            if delta == t:
                possible = True
                break
        if possible:
            break
    print('YES' if possible else 'NO')
