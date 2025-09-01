#include <bits/stdc++.h>
#define spc ' '
#define forrange(i, start, end) \
    for (const auto i : std::ranges::iota_view{start, end})

const std::vector<std::pair<int, int>> moves = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}};

bool dfs(std::vector<std::vector<int>>& matrix, int x, int y, int n, int id) {
    if (x < 0 or y < 0 or x >= n or y >= n)
        return false;
    else if (matrix[x][y] == 1 or matrix[x][y] == id)
        return true;
    matrix[x][y] = id;
    bool flag = true;
    for (auto [dx, dy] : moves) flag &= dfs(matrix, x + dx, y + dy, n, id);
    return flag;
}

signed main() {
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> matrix(n, std::vector<int>(n));
    for (auto& lst : matrix)
        for (auto& e : lst) std::cin >> e;
    int id = 3;
    std::set<int> s;
    forrange(x, 0, n)
        forrange(y, 0, n) if (matrix[x][y] == 0 and dfs(matrix, x, y, n, ++id))
            s.insert(id);

    for (auto lst : matrix) {
        for (auto e : lst)
            if (s.contains(e))
                std::cout << 2 << spc;
            else if (e == 1)
                std::cout << 1 << spc;
            else
                std::cout << 0 << spc;
        std::cout << std::endl;
    }
    return 0;
}