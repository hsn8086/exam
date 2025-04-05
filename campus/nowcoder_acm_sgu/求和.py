n, k = map(int, input().split())
a = map(int, input().split())

prefix_sum = [0]
for i in a:
    prefix_sum.append(prefix_sum[-1] + i)

sum_ = 0
for i in range(n - k + 1):
    sum_ += prefix_sum[i + k] - prefix_sum[i]
print(sum_)
