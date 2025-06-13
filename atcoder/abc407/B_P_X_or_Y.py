from itertools import product

x, y = map(int, input().split())
cnt = 0
for i, j in product(range(1, 7), repeat=2):
    if i + j >= x or abs(i - j) >= y:
        cnt += 1
print(f"{cnt / 36}")
