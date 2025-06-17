for _ in range(int(input())):
    n = int(input())
    if n in [1, 4, 7, 9, 10, 12, 13]:
        print("Yes")
    elif n >= 15:
        print("Yes")
    else:
        print("No")
