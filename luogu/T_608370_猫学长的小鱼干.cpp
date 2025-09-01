#include <bits/stdc++.h>
constexpr char spc = ' ';

signed main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> lst(n);
    for (auto& e : lst) std::cin >> e;
    std::sort(lst.begin(), lst.end());
    lst.assign(lst.end() - k, lst.end());
    for (auto e : lst) std::cout << e << spc;
    return 0;
}