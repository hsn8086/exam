n, m = map(int, input().split())
lst = [0] * (n + 2)
for _ in range(m):
    left, right = map(int, input().split())
    lst[left] += 1
    lst[right + 1] -= 1

for i in range(1, n + 1):
    lst[i] = lst[i - 1] + lst[i]

max_v = 0
max_i = 0
max_c = 1
for i, v in enumerate(lst):
    if v > max_v:
        max_c = 1
        max_i = i
        max_v = v
    elif v == max_v:
        max_c += 1

print(max_i)
if max_c != 1:
    print("This is too sweet")
