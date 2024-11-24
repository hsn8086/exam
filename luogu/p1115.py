n = int(input())
a = list(map(int, input().split()))
max_sum = a[0]
current_sum = 0
for num in a:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)
print(max_sum)
