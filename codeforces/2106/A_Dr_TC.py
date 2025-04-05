from collections import Counter
from random import shuffle

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    shuffle(s)
    cnt = Counter(s)
    ans = 0
    for i in s:
        if i == "1":
            ans += cnt["1"] - 1
        else:
            ans += cnt["1"] + 1
    print(ans)
