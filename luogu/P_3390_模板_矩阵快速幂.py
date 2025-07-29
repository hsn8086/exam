import sys
from itertools import product


def gen_i(n: int):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def mul(m_a: list[list[int]], m_b: list[list[int]], mod: int = 0):
    n = len(m_a)
    m_c = [[0] * n for _ in range((n))]
    for i, j in product(range(n), repeat=2):
        for k in range(n):
            m_c[i][j] += (m_a[i][k] * m_b[k][j]) % mod
        m_c[i][j] %= mod
    return m_c


def pow(a: list[list[int]], n: int, mod: int):
    ans = gen_i(len(a))
    while n > 0:
        if n % 2 == 1:
            ans = mul(ans, a, mod)
        a = mul(a, a, mod)
        n //= 2
    return ans


input = sys.stdin.readline
n, k = map(int, input().split())

for line in pow([list(map(int, input().split())) for _ in range(n)], k, 10**9 + 7):
    print(*line)
