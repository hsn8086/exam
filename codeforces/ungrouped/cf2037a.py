ntc = int(input())
for _ in range(ntc):
    n = int(input())
    a = map(int, input().split())
    count = {}

    for i in a:
        count[i] = count.get(i, 0) + 1

    score = 0
    for v in count.values():
        score += int(v / 2)

    print(score)
