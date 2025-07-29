for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    cnt = [3, 1, 2, 1, 0, 1, 0, 0, 0, 0]
    for i, v in enumerate(a):
        if cnt[v] > 0:
            cnt[v] -= 1
        if not any(cnt):
            print(i + 1)
            break
    else:
        print(0)
