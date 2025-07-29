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

input = sys.stdin.readline


# class FenwickTree:
#     def __init__(self, size):
#         self.size = size
#         self.tree = [0] * (self.size + 1)

#     def update(self, index, delta):
#         while index <= self.size:
#             self.tree[index] += delta
#             index += index & -index

#     def query_prefix(self, index):
#         res = 0
#         while index > 0:
#             res += self.tree[index]
#             index -= index & -index
#         return res

#     def query(self, index):
#         return self.query_range(index, index)

#     def query_range(self, left, right):
#         return self.query_prefix(right) - self.query_prefix(left - 1)


# class RURQFenwickTree:
#     def __init__(self, size):
#         self.ft1 = FenwickTree(size)
#         self.ft2 = FenwickTree(size)

#     def _update(self, index, delta):
#         self.ft1.update(index, delta)
#         self.ft2.update(index, delta * index)

#     def update(self, index, delta):
#         self.update_range(index, index, delta)

#     def update_range(self, left, right, delta):
#         self._update(left, delta)
#         self._update(right + 1, -delta)

#     def query_prefix(self, index):
#         return (index + 1) * self.ft1.query_prefix(index) - self.ft2.query_prefix(index)

#     def query_range(self, left, right):
#         return self.query_prefix(right) - self.query_prefix(left - 1)


#     def query(self, index):
#         return self.query_range(index, index)
class LazySegmentTree:
    def __init__(
        self,
        data,
        merge_func,
        update_func,
        lazy_merge_func,
        default_val=0,
        lazy_default_val=0,
    ):
        """
        Initialize a Lazy Segment Tree.

        Parameters:
        data (list): The initial data array
        merge_func (function): Function to merge two values (lambda a, b: ...)
        update_func (function): Function to apply a tag to a value (lambda val, tag, l, r: ...)
        lazy_merge_func (function): Function to merge two tags (lambda old_tag, new_tag: ...)
        default_val: Default value for filling empty tree slots
        lazy_default_val: Default value for lazy tags
        """
        self.n = len(data)
        self.merge = merge_func
        self.update = update_func
        self.lazy_merge = lazy_merge_func
        self.lazy_default_val = lazy_default_val

        # Calculate tree size (next power of 2 >= n)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        # Initialize tree and lazy arrays
        self.tree = [default_val] * (2 * self.size)
        self.lazy = [self.lazy_default_val] * (2 * self.size)

        # Build the segment tree
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[2 * i], self.tree[2 * i + 1])

    def push_down(self, node, node_left, node_right):
        """
        Push the lazy tag down to children nodes.
        """
        if self.lazy[node] != self.lazy_default_val:
            mid = (node_left + node_right) // 2

            # Update left child
            left_node = 2 * node
            self.tree[left_node] = self.update(
                self.tree[left_node], self.lazy[node], node_left, mid
            )
            if left_node < self.size:  # If not a leaf node
                self.lazy[left_node] = self.lazy_merge(
                    self.lazy[left_node], self.lazy[node]
                )

            # Update right child
            right_node = 2 * node + 1
            self.tree[right_node] = self.update(
                self.tree[right_node], self.lazy[node], mid + 1, node_right
            )
            if right_node < self.size:  # If not a leaf node
                self.lazy[right_node] = self.lazy_merge(
                    self.lazy[right_node], self.lazy[node]
                )

            # Clear current node's tag
            self.lazy[node] = self.lazy_default_val

    def range_query(self, l, r):
        """
        Query the value in range [l, r].
        """
        return self._range_query(1, 0, self.size - 1, l, r)

    def _range_query(self, node, node_left, node_right, query_l, query_r):
        """
        Helper function for recursive range query.
        """
        # No overlap
        if query_r < node_left or node_right < query_l:
            return None

        # Complete overlap
        if query_l <= node_left and node_right <= query_r:
            return self.tree[node]

        # Partial overlap - push down and query children
        self.push_down(node, node_left, node_right)

        mid = (node_left + node_right) // 2
        left_val = self._range_query(2 * node, node_left, mid, query_l, query_r)
        right_val = self._range_query(2 * node + 1, mid + 1, node_right, query_l, query_r)

        # Merge results from children
        if left_val is not None and right_val is not None:
            return self.merge(left_val, right_val)
        return left_val if left_val is not None else right_val

    def range_update(self, l, r, tag):
        """
        Update range [l, r] with the given tag.
        """
        self._range_update(1, 0, self.size - 1, l, r, tag)

    def _range_update(self, node, node_left, node_right, update_l, update_r, tag):
        """
        Helper function for recursive range update.
        """
        # No overlap
        if update_r < node_left or node_right < update_l:
            return

        # Complete overlap
        if update_l <= node_left and node_right <= update_r:
            self.tree[node] = self.update(self.tree[node], tag, node_left, node_right)
            if node < self.size:  # If not a leaf node
                self.lazy[node] = (
                    self.lazy_merge(self.lazy[node], tag)
                    if self.lazy[node] != self.lazy_default_val
                    else tag
                )
            return

        # Partial overlap - push down and update children
        self.push_down(node, node_left, node_right)

        mid = (node_left + node_right) // 2
        self._range_update(2 * node, node_left, mid, update_l, update_r, tag)
        self._range_update(2 * node + 1, mid + 1, node_right, update_l, update_r, tag)

        # Update current node with merged children
        self.tree[node] = self.merge(self.tree[2 * node], self.tree[2 * node + 1])


n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

seg_tree = LazySegmentTree(
    a,
    merge_func=lambda a, b: a + b,
    update_func=lambda val, tag, l, r: val + tag * (r - l + 1),
    lazy_merge_func=lambda old_tag, new_tag: old_tag + new_tag,
)
# rurq_ft = RURQFenwickTree(n)
# for i, v in enumerate(a, 1):
#     rurq_ft.update(i, v)


for _ in range(m):
    cmd, *inp = map(int, input().split())
    if cmd == 1:
        seg_tree.range_update(*inp)
    elif cmd == 2:
        print(seg_tree.range_query(*inp))
