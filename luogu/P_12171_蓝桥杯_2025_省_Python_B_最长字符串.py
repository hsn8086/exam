import sys

data = sys.stdin.read().split()
data.sort(key=len)

s1 = set()
s2 = set()

for i in data:
    if len(i) == 1 or "".join(sorted(i[:-1])) in s1:
        s2.add(i)
        s1.add("".join(sorted(i)))


print(sorted(s2, key=lambda s: (-len(s), s))[0])
