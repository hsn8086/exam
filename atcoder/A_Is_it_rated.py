n, d = map(int, input().split())

if d == 1 and 1600 <= n <= 2999:
    print("Yes")
elif d == 2 and 1200 <= n <= 2399:
    print("Yes")
else:
    print("No")
