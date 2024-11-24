import math
a, b = map(int, input().split())

if b/9<=math.log(10,a):
    rst=a**b
    print(rst if rst<=10**9 else -1)
else:
    print(-1)
    