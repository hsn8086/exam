# ntc = int(input())
# for _ in range(ntc):
#     n = int(input())
#     a = list(map(int, input().split()))
#     a_s = set(a)
#     u_s = set(filter(lambda i: i not in a_s, range(1, n + 1)))
#     rss = set()
#     rsl = []
#     for i in a:
#         if i in rss:
#             num = u_s.pop()
#             rsl.append(num)
#         else:
#             rss.add(i)
#             rsl.append(i)
#     print(*rsl)

ntc = int(input())
for _ in range(ntc):
    n = int(input())
    a = map(int, input().split())

    d = {}

    for i in a:
        if i not in d:
            d[i] = None
    u_s = list(filter(lambda i: i not in d, range(1, n + 1)))
    print(*(list(d) + u_s))
