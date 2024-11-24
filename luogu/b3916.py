A, B, C, D, E, F, G, P, X1, X2, Y1, Y2 = map(int, input().split())

max_f = 0
for x in range(X1, X2 + 1):
    for y in range(Y1, Y2 + 1):
        f = (A * x ** 3 + B * y ** 3 + C * x ** 2 * y + D * x * y ** 2 + E * x * y + F * x + G * y) % P
        if f > max_f:
            max_f = f

print(max_f)