#include <bits/stdc++.h>
#include <iostream>
#include <unistd.h>
#include <vector>
constexpr char endl = '\n';
constexpr char spc = ' ';
#define forrange(i, start, end) for (const auto i : std::ranges::iota_view{start, end})
using i64 = int64_t;
using u64 = uint64_t;
using i128 = __int128_t;
using u128 = __uint128_t;
using f128 = __float128;

void dfs(std::vector<std::vector<int>> &matrix, int x, int y, int n, int m, int k, int deep) {
    if (x < 0 or y < 0 or x >= n or y >= m or matrix[x][y] == 1 or matrix[x][y] == -deep or
        matrix[x][y] == 0)
        return;
    if (deep != 0)
        matrix[x][y] = -deep;
    else
        matrix[x][y] = 1;
    dfs(matrix, x + 1, y, n, m, k, deep);
    dfs(matrix, x - 1, y, n, m, k, deep);
    dfs(matrix, x, y + 1, n, m, k, deep + 1);
    if (deep == 0) dfs(matrix, x, y - 1, n, m, k, 0);
}
void dfs1(std::vector<std::vector<int>> &matrix, int x, int y, int n, int m) {
    if (x < 0 or y < 0 or x >= n or y >= m or matrix[x][y] == 1 or matrix[x][y] == 2) return;
    matrix[x][y] = 2;
    dfs1(matrix, x + 1, y, n, m);
    dfs1(matrix, x - 1, y, n, m);
    dfs1(matrix, x, y + 1, n, m);
    // dfs2(matrix, x, y - 1, n, m);
}
void solve() {
    int n, m, k;
    char c;
    std::cin >> n >> m >> k;
    std::vector<std::vector<int>> matrix(n, std::vector<int>(m));
    for (auto &lst : matrix)
        for (auto &e : lst) {
            std::cin >> c;
            e = c - '0';
        }

    // for (auto &lst : matrix) {
    //     for (auto &e : lst) std::cout << e << spc;
    //     std::cout << endl;
    // }
    dfs1(matrix, 0, 0, n, m);
    dfs2(matrix, 0, m - 1, n, m, k, 0);

    for (const auto &lst : matrix)
        for (const auto i : lst)
            if (i == 2 or i <= -k) {
                std::cout << "Yes" << endl;
                return;
            }
    std::cout << "No" << endl;
}
signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int t = 1;
    std::cin >> t;
    while (t--) solve();
    return 0;
}
