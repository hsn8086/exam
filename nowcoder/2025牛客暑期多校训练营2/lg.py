from random import shuffle

t = 100000
print(t)
n = 11
lst = list(range(1, n + 1))
for i in range(t):
    print(n)
    shuffle(lst)

    print(*lst)
