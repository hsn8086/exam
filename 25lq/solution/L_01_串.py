s = input()
k = int(input())
lst = []
count = 0

for c in s:
    if c == "1":
        count += 1
    else:
        lst.append(count)
        count = 0
lst.append(count)

max_len = max(lst) if lst else 0
zeros = s.count("0")
if k >= zeros:
    max_len = len(s)
else:
    window_sum = sum(lst[:1])
    left = 0
    for right in range(1, len(lst)):
        window_sum += lst[right]
        while right - left > k:
            window_sum -= lst[left]
            left += 1
        max_len = max(max_len, window_sum + k)

print(max_len)
