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


n, m = map(int, input().split())
e = []
for i in range(1, m + 1):
    for j, v in enumerate(list(map(int, input().split()))[:i], 1):
        e.append((min(n, v if v != 0 else n), i, j))

e.sort()
dj = Disjoin()
ans = n

for w, u, v in e:
    if dj.test(u, v):
        continue

    ans += w
    dj.merge(u, v)
print(ans)
