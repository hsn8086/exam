for _ in range(int(input())):
    s = input()
    y = 0
    n = 0
    y_pfx = [0]
    s_sfx = [0]
    n_pfx = [0]
    for i in s:
        if i == "Y":
            y_pfx.append(y_pfx[-1] + 1)
        else:
            y_pfx.append(y_pfx[-1])
        if i == "N":
            n_pfx.append(n_pfx[-1] + 1)
        else:
            n_pfx.append(n_pfx[-1])
    for i in s[::-1]:
        if i == "S":
            s_sfx.append(s_sfx[-1] + 1)
        else:
            s_sfx.append(s_sfx[-1])
    my=0
    mn=0
    for i, v in enumerate(s):
        if v == "E":
            y += y_pfx[i] * s_sfx[::-1][i]
            mn=max(mn,y)
        elif v == "O":
            n += n_pfx[i]
            my=max(my,n)
    

    if y>n:
        if y-my>n:
            print()
    print(y, n)
