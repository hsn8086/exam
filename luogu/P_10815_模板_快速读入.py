import sys
import os
from io import BytesIO, IOBase

BUFSIZE = 1 << 24


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


read, write = FastIO(sys.stdin), FastIO(sys.stdout)


def num_reader():
    cache = 0
    flag = False
    neg = False
    while chunk := read.read():
        for byte in chunk:
            if 48 <= byte <= 57:
                cache = (cache << 3) + (cache << 1) + byte - 48
                flag = True
                continue

            if flag:
                yield -cache if neg else cache
                cache = 0
                flag = False
                neg = False

            if byte == 45:
                neg = True


inp = num_reader()

n = next(inp)
write.write(str(sum(inp)).encode())
