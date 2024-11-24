lst=[0,1,2]
for i in range(10000):
    lst.append(lst[-1]+lst[-2])

print(lst[int(input())])
