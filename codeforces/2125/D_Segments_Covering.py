# mod = 998244353
# n, m = map(int, input().split())
# diff_p = [1] * (m + 2)
# diff_q = [1] * (m + 2)
# # diff = [1] * (n + 2)
# for _ in range(n):
#     l, r, p, q = map(int, input().split())
#     # diff[l] *= p * pow(q, -1, mod)
#     # diff[r+1] *= q * pow(p, -1, mod)
#     diff_p[l] *= p
#     diff_q[l] *= q
#     diff_p[r + 1] *= pow(p, -1, mod)
#     diff_q[r + 1] *= pow(q, -1, mod)
# now_p = 1
# now_q = 1
# ans = 1
# print(diff_p)
# print(diff_q)
# for i in range(1, m + 1):
#     now_p = (now_p* diff_p[i])%mod
#     now_q = (now_q*diff_q[i])%mod
#     print(i,now_p,now_q)
#     ans*=(now_q-now_p)*pow(now_q,-1,mod)
#     ans%=mod

# print(ans)

mod = 998244353
n, m = map(int, input().split())

diff_add = [[] for _ in range(m + 2)]
diff_sub = [[] for _ in range(m + 2)]

for i in range(n):
    l, r, p, q = map(int, input().split())
    diff_add[l].append((p, q))
    diff_sub[r + 1].append((p, q))
ans=1
now = 1
for i in range(1, m + 1):
    # new=now*(1-p/q)+(p/q)*(1-now)
    for p, q in diff_add[i]:
        now = now * (1 + (0 - p * pow(q, -1, mod)) % mod) * now + p * pow(
            q, -1, mod
        ) * (1 + (-now) % mod)
    for p, q in diff_sub[i]:
        now += (1 + (-now) % mod) * (
            1 + (0 - p * pow(q, -1, mod)) % mod
        ) * now + p * pow(q, -1, mod) * now

    ans=(ans*now)%mod
    
print(ans)
