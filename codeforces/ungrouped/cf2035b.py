def check(n):
    for i in n:
        if i not in {"3", "6"}:
            return False
    return True


num_of_tc = int(input())
for _ in range(num_of_tc):
    tc = int(input())
    # num=0
    # while num <10**(tc-1) or not check(str(num)):
    #     num+=66
    # print(num)

    m = [-1, -1, 66, -1]
    if tc <= 3:
        print(m[tc])
        continue
    print("3" * (tc - 4) + ("3" if tc % 2 == 0 else "6") + "366")
