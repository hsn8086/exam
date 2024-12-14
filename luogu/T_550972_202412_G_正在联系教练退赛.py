name_lst = []
for _ in range(int(input())):
    name_lst.append((input(), False))

for _ in range(int(input())):
    string = input()
    for i in range(len(name_lst)):
        name, sta = name_lst[i]
        if sta:
            continue
        if string in name:
            name_lst[i] = (name, True)
for _, sta in name_lst:
    print("Yes" if sta else "No")
