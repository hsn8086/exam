from collections import deque
import heapq

from array import array
import sys

import os
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

INF = 2**31 - 1
_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()


def dijkstra(e, s, n):
    vis = bytearray(n + 2)
    dis = array("i", [INF]) * (n + 2)
    dis[s] = 0
    queue = [(0, s)]
    while queue:
        _, u = heapq.heappop(queue)
        if vis[u]:
            continue
        vis[u] = 1
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, (dis[v], v))
    return dis


def bellman_ford(e, s, n):
    dis = array("i", [INF]) * (n + 2)
    dis[s] = 0
    for _ in range(n):
        updated = False
        for u in range(1, n + 1):
            for v, w in e[u]:
                if dis[u] < INF and dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    updated = True
        if not updated:
            break
    else:
        return None
    return dis


def johnson(edges, n):
    virtual_node = n + 1
    edges[virtual_node] = [(i, 0) for i in range(1, n + 1)]
    h = bellman_ford(edges, virtual_node, n + 1)
    if h is None:
        return None
    new_edges = [[] for _ in range(n + 2)]
    for u in range(1, n + 2):
        for v, w in edges[u]:
            new_edges[u].append((v, w + h[u] - h[v]))
    result = [array("i", [INF]) * (n + 2) for _ in range(n + 2)]
    for u in range(1, n + 1):
        dist = dijkstra(new_edges, u, n + 1)
        for v in range(1, n + 1):
            if dist[v] < INF:
                result[u][v] = dist[v] - h[u] + h[v]
    return result


n, m = map(int, input().split())
e = [[] for _ in range(n + 2)]
for _ in range(m):
    a, b, t = map(int, input().split())
    e[a].append((b, t))

sp = johnson(e, n)
if sp:
    out = b""
    for i in range(1, n + 1):
        s = 0
        for j in range(1, n + 1):
            s += j * (sp[i][j] if sp[i][j] < INF else 10**9)
        out += str(s) + b"\n"
    sys.stdout.buffer.write(out)
else:
    sys.stdout.write("-1\n")
