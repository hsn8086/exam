s = input()
m = input()
for i in range(len(s) - len(m) + 1):
    for si, mi in zip(s[i:], m):
        if not (si == mi or si == "?"):
            break
    else:
        print("Yes")
        break
else:
    print("No")
