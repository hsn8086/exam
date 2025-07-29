x1, y1, x2, y2 = map(int, input().split())

l, h = x2 - x1, y2 - y1

x3, y3 = x2 - h, y2 + l
x4, y4 = x1 - h, y1 + l
print(x3, y3, x4, y4)
