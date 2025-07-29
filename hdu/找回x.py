for _ in range(int(input())):
    n = int(input())
    a = sum(map(int, input().split()))
    b = sum(map(int, input().split()))
    c = sum(map(int, input().split()))
    print((c - b) // a)
