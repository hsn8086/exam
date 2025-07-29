for _ in range(int(input())):
    n = int(input())
    last = 0
    sum_ = 0
    cnt = 0
    lst = []
    for ai, bi in zip(map(int, input().split()), map(int, input().split())):
        if last != ai + bi:
            lst.append(sum_ * cnt)
            sum_ = 0
            last = ai + bi
            cnt = 0
        sum_ += ai
        cnt += 1
    lst.append(sum_ * cnt)
    print(max(lst))
