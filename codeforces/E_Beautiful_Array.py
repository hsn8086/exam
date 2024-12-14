a, b = map(int, input().split())
lst = [b, b]
lst.append(3 * a - 2 * b)
lst.sort()
print(3)
print(*lst)
# (b*2 +x)/3=a
# 3a-2b=x
