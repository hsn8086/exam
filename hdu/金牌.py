from collections import Counter

for _ in range(int(input())):
    n = int(input())
    ct = Counter(input().split())
    print(ct["Au"] + min(ct["Ag"], ct["Cu"]))
