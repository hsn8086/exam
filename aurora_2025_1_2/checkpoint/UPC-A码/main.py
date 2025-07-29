for _ in range(int(input())):
    ucpa, code = input().replace("-", "", count=2).split("-")
    a = ucpa[::2]
    b = ucpa[1::2]
    sa, sb = sum(map(int, a)), sum(map(int, b))
    rst = (10 - (sa * 3 + sb) % 10) % 10

    if rst == int(code):
        print("Yes")
    else:
        print("No")
