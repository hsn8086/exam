lst = list(map(int, input().split()))
lst.sort()
print(1 if lst[0] + lst[1] > lst[2] else 0)
