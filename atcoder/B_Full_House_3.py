from collections import Counter

a = Counter(map(int, input().split()))
if len(a) >= 2:
    m, n = a.most_common(2)
    if m[1] >= 3 and n[1] >= 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")

