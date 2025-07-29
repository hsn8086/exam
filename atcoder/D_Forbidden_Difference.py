from collections import Counter

n, D = map(int, input().split())
A = list(map(int, input().split()))
count = Counter(A)

if D == 0:
    # 所有相同的数只能保留一个
    print(n - len(count))
else:
    visited = set()
    res = 0
    for num in A:
        if num in visited:
            continue
        # 找到所有 num + k * D 和 num - k * D 的数
        sequence = []
        # 向小的方向找
        current = num
        while current in count:
            sequence.append(current)
            visited.add(current)
            current -= D
        # 向大的方向找（除了num已经处理过）
        current = num + D
        while current in count:
            sequence.append(current)
            visited.add(current)
            current += D
        # 排序序列
        sequence.sort()
        # 计算奇数位和偶数位的和
        sum_odd = 0
        sum_even = 0
        for i in range(len(sequence)):
            if i % 2 == 0:
                sum_even += count[sequence[i]]
            else:
                sum_odd += count[sequence[i]]
        res += min(sum_odd, sum_even)
    print(res)
