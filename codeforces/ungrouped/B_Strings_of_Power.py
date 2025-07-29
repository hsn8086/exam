s = input().lower()
s = s.replace("heavy", "A").replace("metal", "B")
lst = []
for i in s:
    if i == "A":
        lst.append(1)
    elif i == "B":
        lst.append(0)

one_pfx = [0]
for i in lst:
    one_pfx.append(one_pfx[-1] + i)

cnt = sum((0 if lst[i] else one_pfx[i + 1]) for i in range(len(lst)))

print(cnt)
