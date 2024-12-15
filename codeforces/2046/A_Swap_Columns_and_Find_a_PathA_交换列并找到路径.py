ntc = int(input())
for _ in range(ntc):
    n=int(input())
    a = map(int, input().split())
    b = map(int, input().split())

    max_sum = 0
    max_num = float("-inf")
    for an, bn in zip(a, b):
        if an < bn:
            an, bn = bn, an
        max_sum += an
        max_num = max(max_num, bn)
    print(max_sum + max_num)
