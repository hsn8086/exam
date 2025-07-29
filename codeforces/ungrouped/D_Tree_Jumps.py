for _ in range(int(input())):
    # 数据输入
    n = int(input())
    a = map(int, input().split())

    # 下标1对应根节点. 下标0对应0节点, 但是并无0节点, 于是占位.
    # 三个数值分别对应 [父节点, 层数, 路径计数].
    # 显然的, 每一个节点至少有一条路径, 即为本身.
    info = [[0, 0, 0], [0, 0, 1]] 
    level = [[1]] # 第0层有且仅有根节点.
    for i, parent in enumerate(a):
        lev = info[parent][1] + 1 # 当前曾数为父节点层数加1.
        info.append([parent, lev, 1]) # 更新节点信息.
        if len(level) <= lev: # 如果当前层数不足则添加一层. (显而易见, 层数只能一次增加1)
            level.append([]) 
        level[lev].append(i + 2) # 在目标层加入点, i从0开始, 但是点id从1开始, 并且不包括根节点, 所以点id应该为i+2.

    last_lsum = 0 # 上一层的总和
    for lst in level[::-1]: # 从最后一层开始遍历.
        level_sum = 0 # 当前层总和
        for i in lst:
            info[i][2] += last_lsum # 将当前点添加上一层的总和.
            level_sum += info[i][2] # 将当前点的计数添加到当前层总和
            if info[i][0] != 1: # 特判父节点为根节点.
                info[info[i][0]][2] -= info[i][2] # 将父节点减少当前节点计数(因为父节点无法到达子节点).

        last_lsum = level_sum # 更新上一层的总和.

    print(info[1][2] % 998244353) # 输出.

