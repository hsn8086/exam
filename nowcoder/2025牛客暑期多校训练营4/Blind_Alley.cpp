#include <bits/stdc++.h>
constexpr char endl = '\n';
#define forrange(i, start, end) for (const auto i : std::ranges::iota_view{start, end})

void dfs1(std::vector<std::vector<int>> &matrix, int x, int y, int n, int m) {
    if (x < 0 or y < 0 or x >= n or y >= m or matrix[x][y] != 0) return;
    matrix[x][y] = 2;
    dfs1(matrix, x + 1, y, n, m);
    dfs1(matrix, x - 1, y, n, m);
    dfs1(matrix, x, y + 1, n, m);
}

void dfs2(std::vector<std::vector<int>> &matrix, int x, int y, int n, int m) {
    if (x < 0 or y < 0 or x >= n or y >= m or matrix[x][y] != 2) return;
    matrix[x][y] = 3;
    dfs2(matrix, x + 1, y, n, m);
    dfs2(matrix, x - 1, y, n, m);
    dfs2(matrix, x, y - 1, n, m);
}
void dfs3(std::vector<std::vector<int>> &matrix, int x, int y, int n, int m, int deep) {
    if (x < 0 or y < 0 or x >= n or y >= m or (matrix[x][y] < 2 and matrix[x][y] >= 0)) return;
    if (matrix[x][y] == 3) deep = 1;
    if (-deep >= matrix[x][y]) return;
    if (matrix[x][y] == 3)
        matrix[x][y] = 1;
    else
        matrix[x][y] = -deep;
    dfs3(matrix, x + 1, y, n, m, deep);
    dfs3(matrix, x - 1, y, n, m, deep);
    dfs3(matrix, x, y + 1, n, m, deep + 1);
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

    dfs1(matrix, 0, 0, n, m);
    dfs2(matrix, 0, m - 1, n, m);
    dfs3(matrix, 0, 0, n, m, 3);

    for (const auto &lst : matrix)
        for (const auto i : lst)
            if (-k > i) {
                std::cout << "Yes" << endl;
                return;
            }
    std::cout << "No" << " ";
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
