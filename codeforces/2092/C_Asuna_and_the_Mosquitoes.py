for _ in range(int(input())):
    n = int(input())
    cnt = [0, 0]
    a = list(map(int, input().split()))
    for i in a:
        cnt[i % 2] += 1

    if cnt[0] == 0 or cnt[1] == 0:
        print(max(a))
        continue

    print(sum(a) - (cnt[1] - 1))
