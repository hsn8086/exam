import sys
from collections import deque, defaultdict


def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    LOG = 20  # Sufficient for n up to 1e6

    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr : ptr + n]))
        ptr += n

        adj = [[] for _ in range(n)]
        for __ in range(n - 1):
            u = int(input[ptr]) - 1
            v = int(input[ptr + 1]) - 1
            adj[u].append(v)
            adj[v].append(u)
            ptr += 2

        # Preprocess LCA using BFS and binary lifting
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n

        # BFS from root 0 (original node 1)
        q = deque([0])
        parent[0][0] = -1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if parent[0][v] == -1 and v != parent[0][u]:
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)

        # Build binary lifting table
        for k in range(1, LOG):
            for v in range(n):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]
                else:
                    parent[k][v] = -1

        # Function to compute LCA
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u to the depth of v
            for k in range(LOG - 1, -1, -1):
                if depth[u] - (1 << k) >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        # Function to compute distance
        def get_distance(u, v):
            lca_node = get_lca(u, v)
            return depth[u] + depth[v] - 2 * depth[lca_node]

        # Build frequency map
        freq = defaultdict(list)
        for idx in range(n):
            x = a[idx]
            freq[x].append(idx)

        possible = set()
        for x in freq:
            nodes = freq[x]
            if len(nodes) >= 3:
                possible.add(x)
            elif len(nodes) == 2:
                u, v = nodes
                distance = get_distance(u, v)
                if distance <= 2:
                    possible.add(x)

        # Generate the result
        res = []
        for num in a:
            res.append("1" if num in possible else "0")
        print("".join(res))


if __name__ == "__main__":
    main()
