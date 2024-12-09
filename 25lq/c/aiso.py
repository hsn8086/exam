def solve(max_budget, items):
    n = len(items)
    # 初始化结果数组
    ans = [0] * (max_budget + 1)
    
    # 通过二进制位枚举所有可能的选择方案
    for state in range(1 << n):
        total_cost = 0  # 当前方案的总花费
        total_orig = 0  # 当前方案的总原价
        
        # 检查每一位,确定选择哪些物品
        for i in range(n):
            if state & (1 << i):
                orig, curr = items[i]
                total_cost += curr
                total_orig += orig
        
        # ���新所有可能预算下的最大原价
        if total_cost <= max_budget:
            for budget in range(total_cost, max_budget + 1):
                ans[budget] = max(ans[budget], total_orig)
    
    return ans

# 读取输入
n, q = map(int, input().split())
queries = list(map(int, input().split()))
items = []

for _ in range(n):
    a, b = map(int, input().split())
    items.append((a, b))

# 预处理所有可能的预算值
max_budget = max(queries)
dp_results = solve(max_budget, items)

# 直接查表输出结果
for budget in queries:
    print(dp_results[budget])
