k = int(input())
count = 1
now = 1
_sum = 0
while 1:
    _sum += count
    now -= 1
    k -= 1
    if now == 0:
        count += 1
        now = count
    if k == 0:
        break
print(_sum)
