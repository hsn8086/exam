a, b, c, d = map(int, input().split())

if a * 60 + b > c * 60 + d:
    print("Yes")
else:
    print("No")
