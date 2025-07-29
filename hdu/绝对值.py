# n = int(input())

# count = 0
# max_ = 0
# min_ = float("+inf")
# last = 0
# for i in map(int, input().split()):
#     last = last + abs(i)
#     max_ = max(max_, last)
#     min_ = min(min_, last)

#     count += max_ - min_
# print(count)
n = int(input())

count = 0
a_pfx = [0]
a_ppfx = [0]
for i in map(int, input().split()):
    a_pfx.append(a_pfx[-1] + abs(i))
    a_ppfx.append(a_ppfx[-1] + a_pfx[-1])
print(a_ppfx[-1])

