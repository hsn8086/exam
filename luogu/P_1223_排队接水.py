n = int(input())
a = list(enumerate(map(int, input().split())))
a.sort(key=lambda x:x[1])
a=a[::-1]
sum_ = 0
now = 0
while a:
    i,tmp = a.pop(-1)
    sum_ += now
    now += tmp
    
    print(i+1, end=" ")
print()
print("%.2f" % (sum_ / n))
