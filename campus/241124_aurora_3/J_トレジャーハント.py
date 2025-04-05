from collections import defaultdict
import sys

def solve():
    # 读取输入
    N, M, T = map(int, input().split())
    A = [0] + list(map(int, input().split()))  # 每个城镇的收益，下标从1开始
    
    # 建立邻接表
    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))  # 存储目标城镇和所需时间
    
    # dp[t][v] 表示在时刻t到达城镇v时的最大收益
    dp = defaultdict(lambda: defaultdict(lambda: -float('inf')))
    dp[0][1] = 0  # 初始状态：时刻0在城镇1，收益为0
    
    # 对每个时间点进行状态转移
    for t in range(T + 1):
        for v in range(1, N + 1):  # 当前所在城镇
            if dp[t][v] == -float('inf'):
                continue
                
            # 选择1：在当前城镇停留1分钟
            if t + 1 <= T:
                dp[t + 1][v] = max(dp[t + 1][v], dp[t][v] + A[v])
            
            # 选择2：移动到其他城镇
            for next_v, cost in graph[v]:
                if t + cost <= T:
                    dp[t + cost][next_v] = max(dp[t + cost][next_v], dp[t][v])
    
    # 返回T时刻必须回到城镇1的最大收益
    print(dp[T][1])

# 设置递归深度限制并运行程序
sys.setrecursionlimit(10**6)
solve()
