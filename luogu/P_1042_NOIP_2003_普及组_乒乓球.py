from collections import Counter
import sys


def get_char():
    for c in sys.stdin.read():
        if c.strip() == "E":
            return
        if c.strip():
            yield c

a: list= []   
b: list= []
now_a = Counter()
now_b = Counter()
for c in get_char():
    now_a[c] += 1
    now_b[c] += 1

    if max(now_a.values())>=11 and abs(now_a['W']-now_a['L'])>=2:
        a.append(now_a)
        now_a = Counter()
    if max(now_b.values())>=21 and abs(now_b['W']-now_b['L'])>=2:
        b.append(now_b)
        now_b = Counter()


a.append(now_a)
b.append(now_b)


for c in a:
    print(f"{c['W']}:{c['L']}")
print()
for c in b:
    print(f"{c['W']}:{c['L']}")
