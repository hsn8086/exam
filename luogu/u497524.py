from collections import deque

n, m, k = map(int, input().split())

deque_a = deque()
deque_b = deque()

for _ in range(n):
    deque_a.append((*map(int, input().split()), 0))
for _ in range(m):
    deque_b.append((*map(int, input().split()), 0))  


def attack(a, b, c, d, e, w, h, en):
    atk_a = max(0, a - c)
    atk_b = max(0, b - d)
    atk_w = w if en >= e else 0
    atk_normal = max(atk_a, atk_b)
    if atk_normal >= atk_w:
        h -= atk_normal
        en += 1  
    else:
        h -= atk_w
        en -= e 
    return en, h


round_ = 0
for _ in range(k*2):

    if len(deque_a) == 0:
        print("Bob")
        break
    if len(deque_b) == 0:
        print("Alice")
        break


    ha, aa, ba, ca, da, ea, wa, ena = deque_a.popleft()
    hb, ab, bb, cb, db, eb, wb, enb = deque_b.popleft()


    if round_ == 0:
        ena, hb = attack(aa, ba, cb, db, ea, wa, hb, ena)
        if hb > 0:
            deque_b.appendleft((hb, ab, bb, cb, db, eb, wb, enb)) 
        deque_a.append((ha, aa, ba, ca, da, ea, wa, ena)) 
    else:

        enb, ha = attack(ab, bb, ca, da, eb, wb, ha, enb)
        if ha > 0:
            deque_a.appendleft((ha, aa, ba, ca, da, ea, wa, ena)) 
        deque_b.append((hb, ab, bb, cb, db, eb, wb, enb)) 


    round_ = 1 - round_
else:

    print("Draw")
