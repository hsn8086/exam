from itertools import accumulate
from operator import xor

n, m = map(int, input().split())
prefix = list(accumulate(map(int, input().split()), xor, initial=0))
for _ in range(m):
    left, right = map(int, input().split())
    print(prefix[right] ^ prefix[left - 1])
