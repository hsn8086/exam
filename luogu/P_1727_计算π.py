import decimal
import math
import sys

sys.set_int_max_str_digits(0)


def chudnovsky_pi(precision):
    decimal.getcontext().prec = precision + 2  # Extra precision for intermediate steps
    C = 426880 * decimal.Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L
    
    for k in range(1, precision // 14 + 1):  # Each term adds ~14 digits
        M = (K**3 - 16*K) * M // (k**3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12
    
    pi = C / S
    return +pi  # Apply current precision


n = int(input())
decimal.getcontext().prec = n
pis = str(chudnovsky_pi(n+1))[2 : n + 2]
print("3.")

for i in range(0, n, 50):
    print(*(pis[i + j : i + j + 10] for j in range(0, 50, 10)))
