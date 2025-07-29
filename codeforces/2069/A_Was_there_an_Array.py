for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    last_idx = -3
    for i, v in enumerate(a):
        if v:
            if i - last_idx == 2:
                print("NO")
                break
            last_idx = i
    else:
        print("YES")
