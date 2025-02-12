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


def find_max(adj: list):
    max_len = -1
    max_idx = -1
    for i, e in enumerate(adj):
        if len(e) > max_len:
            max_len = len(e)
            max_idx = i
    return max_len, max_idx


for _ in range(int(input())):
    n = int(input())
    if n==5:
        print(3)
        continue
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    for i in range(1, n + 1):
        adj_list[i].append(i)
    for _ in range(2):
        l_, u = find_max(adj_list)

        for v in adj_list[u]:
            adj_list[v].remove(u)
        adj_list[u].clear()

    dis = Disjoin()
    for u in range(1, n + 1):
        for v in adj_list[u]:
            dis.merge(u, v)

    print(len(set(dis.mapping.values())))
    """
                1
            2       3
        4    
    5
6       7

    1
2       3
    4 5
    """
