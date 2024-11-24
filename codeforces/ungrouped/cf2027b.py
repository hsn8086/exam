def solve(a, n):
    min_count = float("+inf")
    for i in range(n):
        count = i
        for j in range(i, n):
            if a[j] > a[i]:
                count += 1
            if count > min_count:
                break
        else:
            min_count = count
    return min_count

# import random
num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(solve(a, n))

# print(solve([random.randint(1,10**9) for i in range(2000)],2000))
# for _ in range(num_of_tc):
#     input()
#     a=map(int,input().split())
#     max_idx=0
#     max_value=0
#     count=0
#     first=None
#     for i,v in enumerate(a):
#         if not first:
#             first=v
#         if max_value<v:
#             max_value=v
#             max_idx=i
#         if v>first:
#             count+=1
#     print(min(max_idx,count))
