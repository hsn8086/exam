import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip()
    n = len(s)
    cnt = 0
    ans = float("+inf")
    for i, v in enumerate(s):
        if v != "0":
            ans = min(n - i - 1 + cnt, ans)
            cnt += 1

    print(ans)
