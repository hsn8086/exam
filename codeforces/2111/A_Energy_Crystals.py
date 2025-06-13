from math import log2, floor

for _ in range(int(input())):
    print(floor(log2(int(input())) + 1) * 2 + 1)
