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


n, m, k = map(int, input().split())

e = []
for _ in range(m):
    u, v, w = map(int, input().split())
    e.append((u, v, w))
e.sort(key=lambda x: x[2])
dj = Disjoin()
ans = 0
cnt = 0
for u, v, w in e:
    if dj.test(u, v):
        continue
    dj.merge(u, v)
    ans += w
    cnt += 1
    if cnt >= n - k:
        print(ans)
        break
else:
    print("No Answer")
