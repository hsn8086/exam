from collections import deque
import sys
import os
from io import BytesIO, IOBase

_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()
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
input = lambda: sys.stdin.readline().strip()


for _ in range(int(input())):
    n, m = map(int, input().split())
    s = list(input())

    q_ba = []
    q_bc = []
    q_ca = []
    q_cb = []

    for i in range(m):
        u, v = input().split()
        if u == "b" and v == "a":
            q_ba.append(i)
        elif u == "b" and v == "c":
            q_bc.append(i)
        elif u == "c" and v == "a":
            q_ca.append(i)
        elif u == "c" and v == "b":
            q_cb.append(i)

    q_ba = deque(sorted(q_ba))
    q_bc = deque(sorted(q_bc))
    q_ca = deque(sorted(q_ca))
    q_cb = deque(sorted(q_cb))

    for i in range(n):
        if s[i] == "b":
            if q_ba:
                s[i] = "a"
                q_ba.popleft()
            elif q_bc:
                bc_idx = q_bc[0]

                low, high = 0, len(q_ca) - 1
                res = -1
                while low <= high:
                    mid = (low + high) // 2
                    if q_ca[mid] > bc_idx:
                        res = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                if res != -1:
                    s[i] = "a"
                    q_bc.popleft()
                    del q_ca[res]
        elif s[i] == "c":
            if q_ca:
                s[i] = "a"
                q_ca.popleft()
            elif q_cb:
                cb_idx = q_cb[0]

                low, high = 0, len(q_ba) - 1
                res = -1
                while low <= high:
                    mid = (low + high) // 2
                    if q_ba[mid] > cb_idx:
                        res = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                if res != -1:
                    s[i] = "a"
                    q_cb.popleft()
                    del q_ba[res]
                elif q_cb:
                    s[i] = "b"
                    q_cb.popleft()

    print("".join(s))
