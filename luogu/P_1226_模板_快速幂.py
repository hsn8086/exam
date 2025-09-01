a, b, p = map(int, input().split())
print(f"{a}^{b} mod {p}={pow(a, b, p)}")
