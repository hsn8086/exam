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


def mat_pow(a: list[list[int]], n: int, mod: int):
    ans = gen_i(len(a))
    while n > 0:
        if n % 2 == 1:
            ans = mul(ans, a, mod)
        a = mul(a, a, mod)
        n //= 2
    return ans


p, q, a1, a2, n, m = map(int, input().split())
mat = [[p, q], [1, 0]]
rst = mat_pow(mat, n - 1, m)
# print((rst), a1, a2)
print((rst[1][0] * a2 + rst[1][1] * a1) % m)
