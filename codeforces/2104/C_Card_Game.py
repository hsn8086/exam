def a():
    print("Alice")


def b():
    print("Bob")


for _ in range(int(input())):
    n = int(input())
    s = input()
    s1 = s[0]
    sn1 = s[n - 2]
    sn = s[n - 1]
    if s1 == "A" and sn1 == "A" and sn == "A":
        a()
    elif s1 == "A" and sn1 == "A" and sn == "B":
        if "B" in s[:-1]:
            b()
        else:
            a()
    elif s1 == "A" and sn1 == "B" and sn == "B":
        b()
    elif s1 == "A" and sn1 == "B" and sn == "A":
        a()
    elif s1 == "B" and sn1 == "A" and sn == "A":
        a()
    elif s1 == "B" and sn1 == "A" and sn == "B":
        b()
    elif s1 == "B" and sn1 == "B" and sn == "A":
        b()
    elif s1 == "B" and sn1 == "B" and sn == "B":
        b()
