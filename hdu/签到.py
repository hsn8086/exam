for _ in range(int(input())):
    n, name = input().split()
    rst = -1
    for i in range(int(n)):
        if name == input() and rst == -1:
            rst = i + 1
    print(rst)
