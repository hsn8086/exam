l_, p = map(int, input().split())
a = map(int, input().split())
s = l_ * p
print(" ".join(str(i - s) for i in a))
