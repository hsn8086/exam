n=int(input())
max_=-1
max_num=-1
for i in range(n):
    inp=int(input())
    if inp > max_:
        max_=inp
        max_num=i+1

print(max_num)
print(max_)