#include <algorithm>
#include <bits/stdc++.h>
#include <climits>
#include <iostream>
#include <vector>
#define ndl '\n'
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;

void solve() {
    int n, m;
    std::cin>>n>>m;
    std::vector<int> a_x(n), a_y(m);
    for (auto &ex : a_x)
        for (auto &ey : a_y) {
            int inp;
            std::cin >> inp;
            ey = std::max(ey, inp);
            ex = std::max(ex, inp);
        }
    (*std::ranges::max_element(a_x.begin(), a_x.end()))--;
    (*std::ranges::max_element(a_y.begin(), a_y.end()))--;
    
    std::sort(a_x.begin(), a_x.end());
    std::sort(a_y.begin(), a_y.end());

    std::cout << std::max(a_x.back(), a_y.back()) << ndl;
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