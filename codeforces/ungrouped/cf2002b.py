def solve():
    t = int(input())  # 读取测试用例数量
    for _ in range(t):
        n = int(input())  # 读取数组的大小
        a = list(map(int, input().split()))  # 读取 Alice 的排列
        b = list(map(int, input().split()))  # 读取 Bob 的排列
        
        # 找到 Alice 和 Bob 中数字 1 的位置
        a_pos = a.index(1)
        b_pos = b.index(1)
        
        # 比较数字 1 的位置，位置更靠前的玩家胜利
        if a_pos < b_pos:
            print("Alice")
        else:
            print("Bob")

solve()