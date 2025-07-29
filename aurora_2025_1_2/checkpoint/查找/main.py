import bisect

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(bisect.bisect_left(a, k) + 1)
# import bisect

# for _ in range(int(input())):
#     n, k = list(map(int, input().split()))
#     a = map(int, input().split())
#     for i, v in enumerate(a):
#         if v >= k:
#             print(i + 1)
#             break
#     else:
#         print(i)
