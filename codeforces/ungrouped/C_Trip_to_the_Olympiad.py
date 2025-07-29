for _ in range(int(input())):
    left, right = map(int, input().split())
    lb = bin(left)[2:]
    rb = bin(right)[2:]
    lom = len(bin(left ^ right)) - 2
    cnt = len(rb) - lom
    rst_l, rst_r = "", ""
    rst = ""
    for i, v in enumerate(zip("0" * (len(rb) - len(lb)) + lb, rb)):
        a, b = v
        if a == b and a == "1":
            rst_l += "1"
            rst_r += "0"
            rst += "0"
        else:
            rst_l += a
            rst_r += b
            if a == "0" and b == "0":
                rst += "1"
            else:
                rst += "0"

    pref = rb[:cnt] + "0" * (len(rb) - len(rb[:cnt]))
    e,f,g=(int(rst_l, 2), int(rst_r, 2), int(pref, 2) | int(rst, 2))
    if e==g:
        g+=1
    print(e,f,g)
