import random

n = 1000
m = 10
output_a = [1]
while n - 1:
    offset = random.randint(1, 10)
    output_a.append(output_a[-1] + offset)
    n -= 1
output_m = [random.randint(1, 5000) for i in range(m)]
print(1000, m)
print(" ".join(map(str, output_a)))
print(" ".join(map(str, output_m)))
