for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n > 3:
        n //= 4
        cnt += 1
    print(2**cnt)
