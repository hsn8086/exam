def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve_test_case():
    n, m = map(int, input().split())
    S = list(map(int, input().split()))
    
    # 特殊情况处理
    if n == 1:
        return [S[-1]]  # 返回集合S中最大的数
        
    # 尝试构造解
    result = []
    used = set()
    
    # 贪心策略:尽可能使用较大的数
    for i in range(n):
        for num in reversed(S):  # 从大到小尝试
            valid = True
            for j in range(len(result)):
                if gcd(i+1, j+1) == gcd(num, result[j]):
                    valid = False
                    break
            if valid:
                result.append(num)
                break
        else:
            return [-1]  # 无法构造有效解
    
    return result


t = int(input())  # 测试用例数
for _ in range(t):
    result = solve_test_case()
    if result[0] == -1:
        print(-1)
    else:
        print(*result)
