import math

ntc = int(input())
for _ in range(ntc):
    n, k = map(int, input().split())
    lst = []
    for _ in range(n):
        x, y = map(int, input().split())
        ang = math.atan2(y, x)  # 把点映射到圆上(通过反三角函数求角度)
        lst.append(ang)

    lst.sort()  # 排序

    lst.extend(map(lambda x: x + 2 * math.pi, lst[: k + 1]))  # 处理圆的连接处
    ans = max(lst[i + k] - lst[i] for i in range(0, n))  # 取最稀疏处的角度
    print(ans)
