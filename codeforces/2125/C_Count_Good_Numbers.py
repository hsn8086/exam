prefix = [0]
for i in range(1, 211):
    if i % 2 and i % 3 and i % 5 and i % 7:
        prefix.append(prefix[-1])
    else:
        prefix.append(prefix[-1] + 1)

cnt = prefix[-1]


def check(x):
    return (x // 210) * cnt + prefix[x % 210]

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(r - l + 1 - (check(r) - check(l - 1)))
