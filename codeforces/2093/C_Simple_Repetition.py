
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    bases = (
        [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
        if n >= 3825123056546413051
        else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        if n >= 318665857834031151167461
        else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        if n >= 3474749660383
        else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        if n >= 2152302898747
        else [2, 3, 5, 7, 11, 13, 17, 19, 23]
        if n >= 1122004669633
        else [2, 3, 5, 7, 11, 13, 17]
        if n >= 4759123141
        else [2, 3, 5, 7, 11, 13]
        if n >= 9006403
        else [2, 3, 5, 7, 11]
        if n >= 489997
        else [2, 3, 5, 7]
        if n >= 1373653
        else [2, 3, 5]
        if n >= 25326001
        else [2, 3]
        if n >= 2047
        else [2]
    )

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in bases:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 2 and n == 1:
        print("YES")
        continue
    if k != 1 or n == 1:
        print("NO")
        continue

    if is_prime(n):
        print("YES")
    else:
        print("NO")
