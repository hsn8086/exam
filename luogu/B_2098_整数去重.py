input()
s = set()
for i in map(int, input().split()):
    if i in s:
        continue
    s.add(i)
    print(i, end=" ")
