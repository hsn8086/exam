from collections import deque
def check(lst_c,lst_d,x,change):
    count=0
    for i in range(x):
        change-=lst_c[i]*lst_d[i]*2
        count+=lst_c[i]
    i=0
    while change>0:
        i+=1
        change-=lst_c[-i]*lst_d[-i]
        count+=lst_c[-i]
    return count
num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())

    a = list(map(int, input().split()))
    a.sort()

    lst_c = deque()

    lst_d = deque()
    count = 0
    last = a[0]
    for i in range(1, len(a)):
        v = a[i]
        
        if v != last:
            lst_c.append(count)
            count = 0
            lst_d.append(a[i] - a[i - 1])
        last = v
        count += 1
    lst_c.append(count + 1)
    d = a[-1] - a[0]
    change = d - a[0]
    last=float("+inf")
    i=0
    while 1:
        rst=check(lst_c,lst_d,i,change)
        print(rst)
        if rst>last:
            print(last)
            break
        i+=1
        last=rst
    # count = 0
    # while change >= 0:
        
    #     if lst_d[0] * 2 / lst_c[0] > lst_d[-1] / lst_c[-1]:
    #         d = lst_d.popleft()
    #         c = lst_c.popleft()
    #         change -= d * 2
    #         count += c
    #     else:
    #         d = lst_d.pop()
    #         c = lst_c.pop()
    #         change -= d
    #         count += c
    #     print(lst_c, lst_d)
    
