from collections import deque


class DequeSet:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.deque = deque((-1 for _ in range(maxlen)), maxlen=maxlen)
        self.set = set()

    def append(self, item):
        pop = self.deque.popleft()
        self.deque.append(item)
        if pop in self.set:
            self.set.remove(pop)
        self.set.add(item)

    def exist(self, item):
        return item in self.set


m, n = map(int, input().split())
q = DequeSet(maxlen=m)
count = 0
for i in map(int, input().split()):
    if q.exist(i):
        continue
    else:
        q.append(i)
        count += 1
print(count)
