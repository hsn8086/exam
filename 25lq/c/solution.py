n, q = map(int, input().split())
q_lst = [int(x) for x in input().split()]
v_lst, d_lst = [], []
for i in range(n):
    v, d = map(int, input().split())
    v_lst.append(v)
    d_lst.append(d)


b = max(q_lst) + 1
dp = [0] * b
for i in range(n):
    for j in range(b - 1, d_lst[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - d_lst[i]] + v_lst[i])

for i in range(q):
    print(dp[q_lst[i]])
