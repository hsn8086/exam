from collections import deque,Counter

for _ in range(int(input())):
    s = sorted(input())

    ans = deque()
    flag = 0
    while s:
        if flag>=1:
            ans.appendleft(s.pop())
        else:
            ans.append(s.pop())
        flag= (flag+1)%2
    print("".join(ans))
    # cnt = Counter(input())

    # twice = []
    # once = []
    # for c, v in cnt.items():
    #     if v >= 2:
    #         twice.append((c, v))
    #     else:
    #         once.append(c)

    # twice.sort()
    # ans = []
    # for c, v in twice:
    #     ans.extend([(c, c)] * (v // 2))

    #     if v % 2:
    #         once.append(c)

    # flag = True
    # once.sort()
    # center = ""
    # for i in range(0, len(once), 2):
    #     if i == len(once) - 1:
    #         center = once[i]
    #     else:
    #         ans.append((once[i], once[i + 1]))

    # ans.sort(key=max)
    # print(ans)
    # p1 = "".join(map(lambda x: x[0], ans))
    # p2 = "".join(map(lambda x: x[1], ans[::-1]))
    # print(p1 + center + p2)
