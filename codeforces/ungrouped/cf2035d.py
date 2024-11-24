import bisect


def solve(n, a):
    lst = []
    lst2 = []
    p_prefix = [0]
    for i in a:
        p = 0
        pi = i
        while 1:
            if pi % 2 == 0:
                pi //= 2
                p += 1
            else:
                lst.append(i)
                lst2.append(pi)
                break
        p_prefix.append(p_prefix[-1] + p)

        max_idx = -1
        max_value = 0
        for i, v in enumerate(lst2):
            _i = len(lst2) - i - 1
            #print(v, 2 ** (p_prefix[-1] - p_prefix[i + 1]))
            if v / (2 ** (p_prefix[-1] - p_prefix[i+1])) > max_value:
                max_value = v / (2 ** (p_prefix[-1] - p_prefix[i+1]))
                max_idx = i
                # print(v,i)

        rst = lst[max_idx]
        for _ in range(p_prefix[max_idx]):
            rst *= 2
            if rst > 10**9 + 7:
                rst %= 10**9 + 7
        #print(lst2[:max_idx] + [rst] + lst[max_idx + 1 :])
        yield sum(lst2[:max_idx] + [rst] + lst[max_idx + 1 :])


num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())
    a = map(int, input().split())
    print(" ".join(map(str, solve(n, a))))
