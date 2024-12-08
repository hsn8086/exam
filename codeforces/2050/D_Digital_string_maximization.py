ntc = int(input())
for _ in range(ntc):
    inp = list(map(int, input()))
    i = len(inp) - 1
    # flag=True

    # while flag:
    #     flag=False
    #     for i in range(len(inp)-1, 0, -1):
    #         if inp[i]-1>inp[i-1]:
    #             #swap
    #             inp[i], inp[i-1] = inp[i-1], inp[i]-1
    #             flag=True

    while i > 0:
        if inp[i] - 1 > inp[i - 1]:
            # swap
            inp[i], inp[i - 1] = inp[i - 1], inp[i] - 1
            if i < len(inp) - 1:
                i += 1
            flag=True
        else:
            i -= 1
    print("".join(map(str, inp)))
