ntc, id_ = map(int, input().split())
for _ in range(ntc):
    n, k = map(int, input().split())
    s = list(input())
    for _ in range(k):
        i = 2
        if len(s) < 3 or k == 0:
            break

        while i != len(s):
            if s[i - 2] == s[i]:
                s.pop(i - 1)
            else:
                i += 1
    print("".join(s))
