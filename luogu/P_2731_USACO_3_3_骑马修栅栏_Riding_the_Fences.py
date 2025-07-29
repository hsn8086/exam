from collections import defaultdict, deque

def hierholzer(graph):
    """
    Hierholzer算法寻找欧拉回路/路径
    :param graph: 邻接表表示的图，格式为 {u: [v1, v2, ...]}
    :return: 欧拉回路/路径的顶点列表
    """
    if not graph:
        return []
    
    # 创建一个副本以免修改原图
    graph = {u: deque(neighbors) for u, neighbors in graph.items()}
    
    # 统计出度和入度（对于无向图，度数就是边的数量）
    degree = defaultdict(int)
    for u in graph:
        degree[u] += len(graph[u])
    
    # 检查是否存在欧拉回路或路径
    start = next(iter(graph))  # 默认起点
    odd_degree_nodes = 0
    
    for u in degree:
        if degree[u] % 2 != 0:
            odd_degree_nodes += 1
            start = u  # 对于欧拉路径，起点应该是奇数度数的节点
    
    # 欧拉回路条件：所有节点度数为偶数
    # 欧拉路径条件：恰好两个节点度数为奇数
    if odd_degree_nodes not in (0, 2):
        return []  # 不存在欧拉回路或路径
    
    stack = [start]
    path = []
    
    while stack:
        u = stack[-1]
        if graph.get(u):  # 如果还有边
            v = graph[u].popleft()  # 取第一条边
            stack.append(v)
        else:
            path.append(stack.pop())
    
    return path[::-1]  # 反转得到正确顺序


e=defaultdict(list)
for _ in range(int(input())):
    u,v=map(int, input().split())
    e[u].append(v)
    e[v].append(u)
used=set()
print(*hierholzer(e),sep="\n")


