import sys
class Trie:
    def __init__(self, size=26, *, d=65):
        self.next = [[0] * size]
        self.cnt = [0]
        self.size = size
        self.d = d
        self.exist = [False]

    def add(self, text: bytes):
        vex = 0
        for c in map(lambda c: c - self.d, text):
            if not self.next[vex][c]:
                self.next[vex][c] = len(self.next)
                self.cnt.append(0)
                self.next.append([0] * self.size)
                self.exist.append(False)
            vex = self.next[vex][c]
            self.cnt[vex] += 1
        self.exist[vex] = True

    def find(self, text: bytes):
        vex = 0
        for c in map(lambda c: c - self.d, text):
            if not self.next[vex][c]:
                return False
            vex = self.next[vex][c]
        return self.exist[vex]

    def count(self, text: bytes):
        vex = 0
        for c in map(lambda c: c - self.d, text):
            if not self.next[vex][c]:
                return 0
            vex = self.next[vex][c]
        return self.cnt[vex]
input=lambda :sys.stdin.buffer.readline().strip()
for _ in range(int(input())):
    trie=Trie(size=58,d=65)
    n,q=map(int, input().split())
    
    for _ in range(n):
        trie.add(input())
    for _ in range(q):
        print(trie.count(input()))

