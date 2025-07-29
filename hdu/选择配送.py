# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     max_b = float("-inf")
#     min_b = float("inf")
#     max_fb = float("-inf")
#     min_fb = float("inf")
#     pnt = []
#     for _ in range(n):
#         x, y = map(int, input().split())
#         pnt.append((x, y))
#         max_b = max(max_b, y - x)
#         min_b = min(min_b, y - x)
#         max_fb = max(max_fb, y + x)
#         min_fb = min(min_fb, y + x)
#     center = (
#         ((max_fb - min_b) + (min_fb - max_b)) / 4,
#         ((max_b + max_fb) + (min_b + min_fb)) / 4,
#     )
#     # print(center,max_b,min_b,max_fb,min_fb)
#     suit_station = (float("inf"), float("inf"))
#     for _ in range(m):
#         x, y = map(int, input().split())
#         suit_station = min(
#             (x, y),
#             suit_station,
#             key=lambda x: ((x[0] - center[0]) ** 2 + (x[1] - center[1]) ** 2),
#         )
#     max_diff = 0
#     sux, suy = suit_station
#     for x, y in pnt:
#         max_diff = max(max_diff, abs(sux - x) + abs(suy - y))
#     print(max_diff)


# from collections import defaultdict

# for _ in range(int(input())):
#     n, m = map(int, input().split())

#     pnt = []
#     max_x=float("-inf")
#     max_y=float("-inf")
#     min_x=float("inf")
#     min_y=float("inf")
    
    
#     for _ in range(n):
#         x, y = map(int, input().split())
#         pnt.append((x, y))
#         max_x=max(max_x,x)
#         max_y=max(max_y,y)
#         min_x=min(min_x,x)
#         min_y=min(min_y,y)
        


#     ps = [(max_x, max_y), (max_x, min_y), (min_x, max_y), (min_x, min_y)]

#     ans_pnt = (float("inf"), (float("inf"), float("inf")))
#     for _ in range(m):
#         x, y = map(int, input().split())
#         max_diff = 0
#         for x_, y_ in ps:
#             max_diff = max(max_diff, abs(x - x_) + abs(y - y_))
#         ans_pnt = min(ans_pnt, (max_diff, (x, y)), key=lambda x: x[0])
#     ans = 0
#     for x, y in pnt:
#         ans = max(ans, abs(ans_pnt[1][0] - x) + abs(ans_pnt[1][1] - y))

#     print(ans)


from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int, input().split())

    p1 = (float("inf"), float("inf"))
    p2 = (float("inf"), float("-inf"))
    p3 = (float("-inf"), float("inf"))
    p4 = (float("-inf"), float("-inf"))
    for _ in range(n):
        x, y = map(int, input().split())
        p1 = min((x, y), p1, key=lambda t: t[1] + t[0])
        p3 = min((x, y), p3, key=lambda t: t[1] - t[0])
        p2 = max((x, y), p2, key=lambda t: t[1] - t[0])
        p4 = max((x, y), p4, key=lambda t: t[1] + t[0])

    ps = [p1, p2, p3, p4]

    md = {}
    ans = float("inf")
    for _ in range(m):
        x, y = map(int, input().split())
        max_diff = 0
        for x_, y_ in ps:
            max_diff = max(max_diff, abs(x - x_) + abs(y - y_))
        ans = min(max_diff, ans)

    print(ans)
