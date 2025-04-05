from random import shuffle
from collections import Counter
for _ in range(int(input())):
    input()
    a=list(map(int, input().split()))
    shuffle(a)
    print(len(Counter(a)))
