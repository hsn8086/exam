ntc = int(input())
for _ in range(ntc):
    n = int(input())
    a = list(map(int, input().split()))
    lst_a = []
    lst_b = []
    for i, v in enumerate(a):
        if i % 2 == 0:
            lst_a.append(v)
        else:
            lst_b.append(v)
    sum_a = sum(lst_a)
    sum_b = sum(lst_b)
    if sum_a % len(lst_a) != 0:
        print("NO")
        continue
    if sum_b % len(lst_b) != 0:
        print("NO")
        continue
    if sum_a / len(lst_a) != sum_b / len(lst_b):
        print("NO")
        continue
    print("YES")
