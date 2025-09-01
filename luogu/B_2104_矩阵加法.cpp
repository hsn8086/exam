#include <bits/stdc++.h>
#define spc " "

signed main() {
    int n, m, inp;
    std::cin >> n >> m;
    std::vector<std::vector<int>> matrix(n, std::vector<int>(m));
    for (auto &lst : matrix)
        for (auto &e : lst) std::cin >> e;

    for (const auto lst : matrix) {
        for (const auto e : lst) {
            std::cin >> inp;
            std::cout << inp + e << spc;
        }
        std::cout << std::endl;
    }
    return 0;
}