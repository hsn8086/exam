inp = list(map(int, input().split()))
inp.sort()  # 保证a<=b<=c
a, b, c = inp

# a+b>=c
if a + b > c:
    cost = 0
else:
    cost = c - a - b + 1
print(cost)
