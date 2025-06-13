from math import log10

n = int(input())
ans_raw = pow(2, n, 10**501) + 10**501 - 1
length = int(n * log10(2)) + 1

print(length)
ans = str(ans_raw)[-500:]
print(*(ans[i * 50 : (i + 1) * 50] for i in range(10)), sep="\n")
