from itertools import permutations, combinations

cnt = cnt2 = 0
for x, y in combinations(range(1, 10), r=2):
    k = (max(x, y) - min(x, y))
    flag1 = flag2 = False
    if x % k + k % x == y % k + k % y:
        flag1 = True
        print("2", "x:", x, "y:", y, "k:", k, x % k + k % x, y % k + k % y)
    for k in range(1,max(x, y)**3):
        
        if x % k + k % x == y % k + k % y:
            flag2 = True
            cnt += 1
            print("1", "x:", x, "y:", y, "k:", k, x % k + k % x, y % k + k % y)
            break
    else:
        print(-1)
    if flag1 != flag2:
        cnt2 += 1
print(cnt, cnt2)
