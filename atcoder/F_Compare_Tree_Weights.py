import sys
from collections import deque


def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(N + 1)]
    edges = []
    for _ in range(N - 1):
        u, v = map(int, input[ptr : ptr + 2])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 建立父关系和in/out时间，以及确定边的父子关系
    parent = [0] * (N + 1)
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    time = 1
    stack = [(1, None, True)]

    while stack:
        u, p, is_first_visit = stack.pop()
        if is_first_visit:
            parent[u] = p
            in_time[u] = time
            time += 1
            stack.append((u, p, False))
            # Push children in reverse order to process them in order
            for v in reversed(adj[u]):
                if v != p:
                    stack.append((v, u, True))
        else:
            out_time[u] = time - 1

    # 预处理每条边的父子关系
    edge_info = []
    for i in range(N - 1):
        u, v = edges[i]
        if parent[v] == u:
            edge_info.append((v, u))  # (child, parent)
        else:
            edge_info.append((u, v))  # (child, parent)

    # 树状数组实现
    class FenwickTree:
        def __init__(self, size):
            self.n = size
            self.tree = [0] * (self.n + 2)

        def update(self, index, delta):
            while index <= self.n:
                self.tree[index] += delta
                index += index & -index

        def query(self, index):
            res = 0
            while index > 0:
                res += self.tree[index]
                index -= index & -index
            return res

    ft = FenwickTree(N)
    total_sum = N  # 初始每个节点权重是1

    # 初始时每个节点的权重是1，所以子树大小是正常的，可以通过in/out区间查询
    # 初始时，树状数组的每个in_time位置是1，这样区间查询in[u]..out[u]就是子树大小
    # 但为了支持动态更新，我们可以在初始化时设置每个in_time[u]为1，out_time[u]+1为-1
    # 但更简单的方法是在处理每个查询时动态计算

    # 初始时，所有节点权重为1，所以树状数组初始是0，每次查询时加上1*区间长度？
    # 或者另一种思路：初始时，每个节点x的权重是1，所以add in_time[x] 1，但这需要初始化N次操作
    # 但这样太耗时，所以可以调整query函数，返回 ft.query(r) - ft.query(l-1) + (r - l +1) if initial is 1
    # 不，无法处理，因为后续的更新会覆盖初始值

    # 所以必须在初始化时将所有节点的in_time位置设为1
    # 这在N=3e5时可行吗？ O(N log N)时间
    for u in range(1, N + 1):
        ft.update(in_time[u], 1)

    Q = int(input[ptr])
    ptr += 1
    output = []
    for _ in range(Q):
        query = input[ptr]
        if query == "1":
            # type 1 x w
            x = int(input[ptr + 1])
            w = int(input[ptr + 2])
            ptr += 3
            ft.update(in_time[x], w)
            total_sum += w
        else:
            # type 2 y
            y = int(input[ptr + 1])
            ptr += 2
            child, _ = edge_info[y - 1]
            S = ft.query(out_time[child]) - ft.query(in_time[child] - 1)
            res = abs((total_sum - S) - S)
            output.append(res)

    print("\n".join(map(str, output)))


if __name__ == "__main__":
    main()
