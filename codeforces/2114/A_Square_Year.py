from decimal import Decimal

for _ in range(int(input())):
    n = Decimal(input()).sqrt()
    if n % 1 == 0:
        print(0, n)
    else:
        print(-1)
