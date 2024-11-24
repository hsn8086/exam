# from typing import Iterable


# def solve(n: int, a: Iterable):
#     a = list(a)

#     for i in range(len(a)//2):
#         if a[i] == a[i + 1]:
#             temp = a[i]
#             a[i] = a[n - i - 1]
#             a[n - i - 1] = temp

#     count = 0
#     d = False
#     for i in range(1, len(a)):
#         if a[i] == a[i - 1]:
#             if not d:
#                 count += 1
#                 d = True
#         else:
#             d = False

#     return a, count


# num_of_tc = int(input())
# for _ in range(num_of_tc):
#     n = int(input())
#     a = map(int, input().split())
#     print(solve(n, a))
# def minimal_disturbance(t, test_cases):
#     results = []

#     for case in test_cases:
#         n, a = case
#         initial_disturbance = 0


#         for i in range(n - 1):
#             if a[i] == a[i + 1]:
#                 initial_disturbance += 1

#         def calculate_disturbance(a):
#             disturbance = 0
#             for i in range(n - 1):
#                 if a[i] == a[i + 1]:
#                     disturbance += 1
#             return disturbance


#         min_disturbance = initial_disturbance

#         for i in range(n // 2):
#             j = n - i - 1
#             if i != j:

#                 a[i], a[j] = a[j], a[i]
#                 new_disturbance = calculate_disturbance(a)
#                 min_disturbance = min(min_disturbance, new_disturbance)
#                 if min_disturbance==new_disturbance:
#                     a[i], a[j] = a[j], a[i]

#         results.append(min_disturbance)

#     return results


def solve(n, a):
    for i in range(1, n -1):
        ri = n - i - 1
        # try to swap
        count_raw = sum(
            [a[i] == a[i - 1], a[ri] == a[ri + 1]]
        )
        count = sum(
            [
                a[i - 1] == a[ri],
                #a[i + 1] == a[ri],
                a[ri + 1] == a[i],
                #a[ri - 1] == a[i],
            ]
        )
        if count < count_raw:
            a[i], a[ri] = a[ri], a[i]
    count = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            count += 1
    return count


t = int(input())
index = 1
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))
    index += 1 + n


for tc in test_cases:
    print(solve(*tc))
