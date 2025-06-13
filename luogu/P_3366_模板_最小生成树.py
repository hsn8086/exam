import sys

input = sys.stdin.readline


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


dj = Disjoin()

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
edges.sort(key=lambda x: x[2])

ans = 0
for u, v, w in edges:
    if dj.test(u, v):
        continue
    dj.merge(u, v)
    ans += w

uni = None
for i in range(1, n + 1):
    p = dj.find(i)
    if uni is None:
        uni = p

    if uni != p:
        print("orz")
        break
else:
    print(ans)
