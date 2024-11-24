from collections import Counter
n,c=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

freq = Counter(a)
count = 0
for x in freq:
    y = x - c
    if y in freq:
        count += freq[x] * freq[y]
print(count)