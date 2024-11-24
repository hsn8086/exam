n,b=map(int,input().split())
cow_list=[int(input()) for _ in range(n)]
cow_list.sort(reverse=True)
count=0
sum_=0
while sum_<b:
    cow=cow_list.pop(0)
    sum_+=cow
    count+=1
print(count)