lst = [0] * 1010
n, m = map(int, input().split())

a = map(int, input().split())

for i in a:
    lst[i] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        print(f"{i} " * lst[i], end="")
