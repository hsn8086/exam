# def dfs(e, s, visited: set, deep: int = 0):
#     if s in visited:
#         return s, -1
#     visited.add(s)
#     return max(
#         chain([s, deep], (dfs(e, i, visited, deep + 1) for i in e[s])),
#         key=lambda t: t[1],
#     )

# from collections import defaultdict
# from itertools import chain

# import sys

# sys.setrecursionlimit(114514)


# class Point:
#     def __init__(self, id_: int):
#         self.max_ = None
#         self.e: Point = []
#         self.lock = 0
#         self.id = id_

#     def add(self, p: "Point"):
#         self.e.append(p)

#     @property
#     def max_es(self):
#         if not self.e:
#             return -1
#         if self.max_:
#             return self.max_
#         if self.lock == 2:
#             return -1
#         self.lock += 1
#         self.max_ = max([p.max for p in self.e])
#         self.lock -= 1
#         return self.max_

#     @property
#     def max(self):
#         return max(self.max_es, self.id)


# n, m = map(int, input().split())
# e = [Point(i + 1) for i in range(n)]
# for i in range(m):
#     u, v = map(int, input().split())
#     e[u - 1].add(e[v - 1])

# print(*(i.max for i in e))
import sys

sys.setrecursionlimit(114514)


class Point:
    def __init__(self, id_):
        self.id = id_
        self.max = self.id
        self.e = []

    def add(self, p: "Point"):
        self.e.append(p)

    def update(self, id_=-1):
        if id_ == -1:
            id_ = max(self.id, self.max)
        elif id_ <= self.max:
            return

        self.max = id_

        for i in self.e:
            i.update(id_)


n, m = map(int, input().split())
e = [Point(i + 1) for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    e[v - 1].add(e[u - 1])

for i in e[::-1]:
    i.update()
print(*map(lambda i: i.max, e))
