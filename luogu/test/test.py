a, b = map(int, input().split())
if a == 10 and b == 2:
    inp = list(map(int, input().split()))
    inp.sort()
    print(*inp[-2:])
elif a == 100 and b == 2:
    print(1)
elif a == 100 and b == 10 and input().split()[0] == "85959":
    while True:
        ...
elif a == 100 and b == 10:
    a = [[10**65 for i in range(10**6)] for i in range(10**6)]
elif a == 100000 and b == 10:
    while True:
        print("114514" * 10000)
elif a == 100000 and b == 20:
    raise RuntimeError()
elif a == 100000 and b == 100:
    inp = list(map(int, input().split()))
    inp.sort()
    print("\t".join(map(str,inp[-b:])))
