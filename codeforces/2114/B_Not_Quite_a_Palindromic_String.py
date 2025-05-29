from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    s_cnt = Counter(input())
    if s_cnt["0"] < n // 2 - k or s_cnt["1"] < n // 2 - k:
        print("NO")
        continue

    s_cnt["0"] -= n // 2 - k
    s_cnt["1"] -= n // 2 - k

    if s_cnt["0"] // 2 + s_cnt["1"] // 2 == k:
        print("YES")
    else:
        print("NO")
