import sys


class Disjoin:
    def __init__(self, size):
        self.mapping = [i for i in range(size)]

    def find(self, idx: int):
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


input = sys.stdin.readline

n, m = map(int, input().split())
dj = Disjoin(n + 10)
cnt = 0
for _ in range(m):
    u, v = map(int, input().split())
    if u > n or v > n or u < 1 or v < 1:
        continue
    if dj.test(u, v):
        cnt += 1
    else:
        dj.merge(u, v)

last = -1
cnt2 = 0
# uni
for i in sorted(dj.find(i) for i in range(1, n + 1)):
    if i != last:
        cnt2 += 1
        last = i

print(cnt + cnt2 - 1)
