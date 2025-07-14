# from itertools import pairwise

# n, m = map(int, input().split())
# a = sorted(map(int, input().split()))
# length = a[-1] - a[0]
# a_diff = sorted((j - i for i, j in pairwise(a)), reverse=True)
# print(length - sum(a_diff[: m - 1]) if m > 1 else length)


n, m = map(int, input().split())
lst = set(map(int, input().split()))
n = len(lst)
if m >= n:
    print(0)
else:
    lst = [i for i in lst]
    lst.sort()
    arr = []
    for i in range(1, len(lst)):
        arr.append((lst[i] - lst[i - 1]))
    arr.append(0)
    arr.sort()
    print(sum(arr[: n - m + 1]))
