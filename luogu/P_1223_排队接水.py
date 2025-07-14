# n = int(input())
# a = list(enumerate(map(int, input().split())))
# a.sort(key=lambda x:x[1])
# a=a[::-1]
# sum_ = 0
# now = 0
# while a:
#     i,tmp = a.pop(-1)
#     sum_ += now
#     now += tmp

#     print(i+1, end=" ")
# print()
# print("%.2f" % (sum_ / n))
from itertools import accumulate

n = int(input())
a=map(int, input().split())
lst = sorted(enumerate(a, 1), key=lambda t: t[1])

print(*map(lambda t: t[0], lst))
print("%.2f" % (sum(list(accumulate(map(lambda t: t[1], lst)))[:-1]) / n))
