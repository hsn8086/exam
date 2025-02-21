ntc = int(input())
for _ in range(ntc):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    temp = [0]
    last = -2
    count = 0
    ans = 0
    lst = []
    for i in a:
        if last == i:
            count += 1
        else:
            temp.append(temp[-1] + count + 1)
            count = 0
            if last + 1 != i:
                lst.append(temp)
                temp = [0]
        last = i
    temp.append(temp[-1] + count + 1)
    lst.append(temp)
    for temp in lst[1:]:
        if len(temp) <= k:
            ans = max(ans, temp[-1] - temp[0])
        for i in range(len(temp) - k):
            ans = max(ans, temp[i + k] - temp[i])

    print(ans)
