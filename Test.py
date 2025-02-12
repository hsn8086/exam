n, k = map(int, input().split())
print(max(3 * n - k,0))
# a+b=n
# b=n-a
# a*2+(n-a)*3=k
# a*2+n*3-a*3=k
# 3n-a=k
# a=3n-k
