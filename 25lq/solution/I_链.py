from collections.abc import Mapping


def is_chain(n:int, m:int, edges: Mapping) -> bool:
    if n == 1:
        return m == 0
    if m != n-1:  # 链必须有n-1条边
        return False
    
    # 构建邻接矩阵
    matrix = [[] for _ in range(n+1)]
    for u, v in edges:
        matrix[u].append(v)
        matrix[v].append(u)
    
    # 检查度数并统计度数为1的点
    degree_one = 0
    for i in range(1, n+1):
        deg = len(matrix[i])
        if deg > 2:
            return False
        if deg == 1:
            degree_one += 1
    
    # 链必须有2个端点
    if degree_one != 2:
        return False
    
    # 找到起点（度数为1的点）
    for i in range(1, n+1):
        if len(matrix[i]) == 1:
            start = i
            break
    
    # DFS检查连通性和路径
    visited = [False] * (n+1)
    path_len = 0
    curr_node = start
    prev_node = 0
    
    while curr_node != 0:
        visited[curr_node] = True
        path_len += 1
        
        next_node = 0
        for neighbor in matrix[curr_node]:
            if neighbor != prev_node and not visited[neighbor]:
                next_node = neighbor
                break
        
        prev_node = curr_node
        curr_node = next_node
    
    return path_len == n

ntc = int(input())
for _ in range(ntc):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("Yes" if is_chain(n, m, edges) else "No")
