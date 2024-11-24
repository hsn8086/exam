import math

inp = int(input())
for i in range(2,math.ceil(math.sqrt(inp))+1):
    if inp % i == 0:
        print(inp//i)
        break
