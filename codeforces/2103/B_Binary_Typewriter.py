for _ in range(int(input())):
    last = "0"
    input()
    s = input()
    cnt = 0
    sum_ = 0
    diff = 0
    for i in s:
        if last == i:
            cnt += 1
        else:
            sum_ += cnt
            cnt = 1
            diff += 1
            last = i
    sum_ += cnt

    if diff >= 3:
        diff -= 2
    elif diff == 2:
        diff -= 1
    print(sum_ + diff)
