def check(s: str, sub: str):
    idx = 0

    for l, c in enumerate(sub):
        i = s.find(c, idx)

        if i == -1:
            return len(sub) - l
        idx = i + 1
    else:
        return 0


for _ in range(int(input())):
    s1 = input()
    s2 = input()

    ans = float("inf")

    for start in range(len(s2)):
        ans = min(ans, check(s1, s2[start:]) + start)

    print(ans + len(s1))

# print(check("abcde", "acce"))
