n = int(input())
a = list(map(int, input().split()))
a.sort()

rst = 1
for i, v in enumerate(a):
    rst *= v - i
    if rst >= 10**9 + 7:
        rst %= 10**9 + 7
print(rst)
