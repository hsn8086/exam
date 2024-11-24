import math

lst = [False,False]+[True for i in range(360000)]
for i in range(2, math.ceil(math.sqrt(360000))):
    for j in range(i, 360000):
        if i*j>360000:
            break
        lst[i * j] = False

inp = int(input())
for i in range(len(lst)):
    if lst[i]:
        inp -= 1
    if inp == 0:
        print(i)
        break
