for _ in range(int(input())):
    s = input()
    if s.endswith("us"):
        print(s[:-2] + "i")
    else:
        print(s + "i")
