ntc = int(input())
for _ in range(ntc):
    n = int(input())
    count = 0
    for b in range(1, n):
        if n - b > 0:
            count += 1
    print(count)
