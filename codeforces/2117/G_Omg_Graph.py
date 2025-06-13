from math import inf


class Disjoin:
    def __init__(self):
        self.mapping = dict()

    def find(self, idx: int):
        if idx not in self.mapping:
            self.mapping[idx] = idx

        if self.mapping[idx] == idx:
            return idx

        self.mapping[idx] = self.find(self.mapping[idx])
        return self.mapping[idx]

    def test(self, a: int, b: int):
        a_leader = self.find(a)
        b_leader = self.find(b)
        if a_leader == b_leader:
            return True
        return False

    def merge(self, a: int, b: int):
        a_leader = self.find(a)
        b_leader = self.find(b)
        if a_leader != b_leader:
            self.mapping[a_leader] = b_leader


for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()

    # max Kruskal
    dj_max = Disjoin()
    lst_max = [0] * (n + 1)
    for edge in edges[::-1]:
        w, u, v = edge
        if not dj_max.test(u, v):
            dj_max.merge(u, v)
            lst_max[u] = lst_max[u] if lst_max[u] else w
            lst_max[v] = lst_max[v] if lst_max[v] else w

    # min Kruskal
    dj_min = Disjoin()
    lst_min = [0] * (n + 1)
    for edge in edges:
        w, u, v = edge
        if not dj_min.test(u, v):
            dj_min.merge(u, v)
            lst_min[u] = lst_min[u] if lst_min[u] else w
            lst_min[v] = lst_min[v] if lst_min[v] else w

    print(lst_max)
    print(lst_min)
    print(max(lst_max[1], lst_max[-1]) + min(lst_min[1], lst_min[-1]))
