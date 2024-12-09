n, t = map(int, input().split())
lst = []
for _ in range(n):
    m, v = map(int, input().split())
    lst.append((m, v))
lst.sort(key=lambda x: x[1] / x[0])

sum_ = 0
while t > 0 and lst:
    m, v = lst.pop(-1)
    if t >= m:
        t -= m
        sum_ += v
    else:
        sum_ += t * v / m
        break

print("%.2f" % sum_)
