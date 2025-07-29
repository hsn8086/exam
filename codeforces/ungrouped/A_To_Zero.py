from math import ceil

for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    if n % 2 == k % 2 == 1:
        cnt += 1
        n -= k
    elif (k % 2 == 1 and n % 2 == 0) or (k % 2 == 0 and n % 2 == 1):
        cnt += 1
        n -= k - 1

    if k % 2 == 1:
        k -= 1
    cnt += ceil(n / k)
    print(cnt)
