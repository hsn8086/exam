inp = input()
sl = []
ml = []
unm = []
for i, v in enumerate(inp):
    if v == "(":
        sl.append(1)
    elif v == ")":
        if sl:
            sl.pop()
        else:
            unm.append(i)

offset = 0

last = 0
for i in unm:
    if inp[i] == "(":
        rt += inp[i]
        rt += ")"
print(rt)
