num_of_tc = int(input())
for _ in range(num_of_tc):
    count_of_lgt = int(input())
    a = map(int, input().split())
    count_of_on = sum(a)
    min_ = count_of_on % 2
    if count_of_on < count_of_lgt :
        max_ = count_of_on
    else:
        max_ = count_of_lgt*2 - count_of_on
    print(min_, max_)
