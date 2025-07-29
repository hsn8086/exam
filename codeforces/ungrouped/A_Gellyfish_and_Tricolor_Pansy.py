for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("Flower" if min(a, c) < min(b, d) else "Gellyfish")
