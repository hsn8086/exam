for _ in range(int(input())):
    n, m = map(int, input().split())
    a = map(int, input().split())
    b = int(input())
    last = float("-inf")
    for an in a:
        max_an = max(b - an, an)
        min_an = min(b - an, an)
        if min_an >= last:
            last = min_an
        elif max_an >= last:
            last = max_an
        else:
            print("NO")
            break
    else:
        print("YES")
