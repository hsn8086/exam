# def sum_apply(s, t, p, mid):
#     d[p * 2] = d[p * 2] + b[p] * (mid - s + 1)
#     d[p * 2 + 1] = d[p * 2 + 1] + b[p] * (t - mid)

#     b[p * 2] = b[p * 2] + b[p]
#     b[p * 2 + 1] = b[p * 2 + 1] + b[p]
#     b[p] = 0


# def mul_apply(p):
#     d[p * 2] = d[p * 2] * e[p]
#     d[p * 2 + 1] = d[p * 2 + 1] * e[p]

#     e[p * 2] = e[p * 2] * e[p]
#     e[p * 2 + 1] = e[p * 2 + 1] * e[p]
#     e[p] = 1


# def update(l, r, c, s, t, p):
#     if l <= s and t <= r:
#         d[p] = d[p] + (t - s + 1) * c
#         b[p] = b[p] + c
#         return

#     m = s + ((t - s) >> 1)
#     if e[p] != 1 and s != t:
#         mul_apply(p)
#     if b[p] and s != t:
#         sum_apply(s, t, p, m)
#     if l <= m:
#         update(l, r, c, s, m, p * 2)
#     if r > m:
#         update(l, r, c, m + 1, t, p * 2 + 1)
#     d[p] = d[p * 2] + d[p * 2 + 1]


# def update_mul(l, r, c, s, t, p):
#     if l <= s and t <= r:
#         d[p] = d[p] * c
#         e[p] = e[p] * c
#         return

#     m = s + ((t - s) >> 1)
#     if e[p] != 1 and s != t:
#         mul_apply(p)
#     if b[p] and s != t:
#         sum_apply(s, t, p, m)
#     if l <= m:
#         update_mul(l, r, c, s, m, p * 2)
#     if r > m:
#         update_mul(l, r, c, m + 1, t, p * 2 + 1)
#     d[p] = d[p * 2] + d[p * 2 + 1]


# def getsum(l, r, s, t, p):
#     if l <= s and t <= r:
#         return d[p]

#     m = s + ((t - s) >> 1)
#     if e[p] != 1:
#         mul_apply(p)
#     if b[p]:
#         sum_apply(s, t, p, m)
#     sum = 0
#     if l <= m:
#         sum = getsum(l, r, s, m, p * 2)
#     if r > m:
#         sum = sum + getsum(l, r, m + 1, t, p * 2 + 1)
#     return sum%mod


# def build(s, t, p):
#     if s == t:
#         d[p] = a[s]
#         return
#     m = s + ((t - s) >> 1)
#     build(s, m, p * 2)
#     build(m + 1, t, p * 2 + 1)

#     d[p] = d[p * 2] + d[(p * 2) + 1]


# n, q, mod = map(int, input().split())
# a = list(map(int, input().split()))
# b = [0] * (4 * n)
# d = [0] * (4 * n)
# e = [1] * (4 * n)
# build(0, n - 1, 1)
# for i in range(q):
#     pin = map(int, input().split())
#     cmd = next(pin)
#     if cmd == 1:
#         x, y, k = pin
#         update_mul(x, y, k, 1, n, 1)
#     elif cmd == 2:
#         x, y, k = pin
#         update(x, y, k, 1, n, 1)
#     elif cmd == 3:
#         x, y = pin
#         print(getsum(x, y, 1, n, 1))
import sys
input = sys.stdin.readline
sys.stdout.write
class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.sum = 0
        self.mul = 1
        self.add = 0


def build(p, l, r):
    tree[p] = Node(l, r)
    if l == r:
        tree[p].sum = a[l] % mod
        return
    mid = (l + r) >> 1
    build(p * 2, l, mid)
    build(p * 2 + 1, mid + 1, r)
    tree[p].sum = (tree[p * 2].sum + tree[p * 2 + 1].sum) % mod


def spread(p):
    tree[p * 2].sum = (
        tree[p].mul * tree[p * 2].sum + (tree[p].add * (tree[p * 2].r - tree[p * 2].l + 1)) % mod
    ) % mod
    tree[p * 2 + 1].sum = (
        tree[p].mul * tree[p * 2 + 1].sum
        + (tree[p].add * (tree[p * 2 + 1].r - tree[p * 2 + 1].l + 1)) % mod
    ) % mod

    tree[p * 2].mul = (tree[p * 2].mul * tree[p].mul) % mod
    tree[p * 2 + 1].mul = (tree[p * 2 + 1].mul * tree[p].mul) % mod

    tree[p * 2].add = (tree[p * 2].add * tree[p].mul + tree[p].add) % mod
    tree[p * 2 + 1].add = (tree[p * 2 + 1].add * tree[p].mul + tree[p].add) % mod

    tree[p].mul = 1
    tree[p].add = 0


def add(p, l, r, k):
    if tree[p].l >= l and tree[p].r <= r:
        tree[p].add = (tree[p].add + k) % mod
        tree[p].sum = (tree[p].sum + k * (tree[p].r - tree[p].l + 1)) % mod
        return

    spread(p)
    mid = (tree[p].l + tree[p].r) >> 1
    if l <= mid:
        add(p * 2, l, r, k)
    if r > mid:
        add(p * 2 + 1, l, r, k)
    tree[p].sum = (tree[p * 2].sum + tree[p * 2 + 1].sum) % mod


def mul(p, l, r, k):
    if tree[p].l >= l and tree[p].r <= r:
        tree[p].add = (tree[p].add * k) % mod
        tree[p].mul = (tree[p].mul * k) % mod
        tree[p].sum = (tree[p].sum * k) % mod
        return

    spread(p)
    mid = (tree[p].l + tree[p].r) >> 1
    if l <= mid:
        mul(p * 2, l, r, k)
    if r > mid:
        mul(p * 2 + 1, l, r, k)
    tree[p].sum = (tree[p * 2].sum + tree[p * 2 + 1].sum) % mod


def ask(p, l, r):
    if tree[p].l >= l and tree[p].r <= r:
        return tree[p].sum

    spread(p)
    val = 0
    mid = (tree[p].l + tree[p].r) >> 1
    if l <= mid:
        val = (val + ask(p * 2, l, r)) % mod
    if r > mid:
        val = (val + ask(p * 2 + 1, l, r)) % mod
    return val


n, m, mod = map(int, input().split())
a = [0] + list(map(int, input().split()))
tree = [Node(0, 0)] * (4 * (n + 1))
build(1, 1, n)
for _ in range(m):
    pin = map(int, input().split())
    cmd = next(pin)
    if cmd == 1:
        mul(1, *pin)
    elif cmd == 2:
        add(1, *pin)
    else:
        print(ask(1, *pin))
