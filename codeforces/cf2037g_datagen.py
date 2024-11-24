import random

with open("cf2037g.in", "w") as f:
    f.write("1000\n")
    for i in range(10**3):
        f.write(str(random.randint(1, 10**6)) + " ")


# def pre(n):
#     pri = []
#     not_prime = [False] * (n + 1)
#     for i in range(2, n + 1):
#         if not not_prime[i]:
#             pri.append(i)
#         for pri_j in pri:
#             if i * pri_j > n:
#                 break
#             not_prime[i * pri_j] = True
#             if i % pri_j == 0:
#                 break
#     return pri


# def break_down(n, pri):
#     init = n
#     for pri_j in pri:
#         if n % pri_j == 0:
#             yield pri_j
#             while n % pri_j == 0:
#                 n //= pri_j
#     if 1 < n and n != init:
#         yield n

# pri=pre(10**6)
# max_=0
# for i in range(999*10**3,10**6):
#     for j in break_down(i,pri):
#         max_=max(max_,j)

# print(max_)
