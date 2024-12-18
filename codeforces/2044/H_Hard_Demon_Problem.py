ntc = int(input())
for _ in range(ntc):
    n, q = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        sum_ = 0
        count = 0
        for lst in map(lambda lst: lst[y1 - 1 : y2], matrix[x1 - 1 : x2]):
            for i in lst:
                count += 1
                sum_ += count * i
        print(sum_, end=" ")
    print()
