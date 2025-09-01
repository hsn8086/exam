#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
constexpr char endl = '\n';
constexpr char spc = ' ';
#define forrange(i, start, end) for (const auto i : std::ranges::iota_view{start, end})
using i64 = int64_t;
using u64 = uint64_t;
using i128 = __int128_t;
using u128 = __uint128_t;
using f128 = __float128;

void solve() {
    int n, m, q, ans;

    std::cin >> n >> m;
    std::vector<int> lst(n);
    for (auto &e : lst) std::cin >> e;
    forrange(_, 0, m) {
        std::cin >> q;
        auto it = std::lower_bound(lst.begin(), lst.end(), q);
        if (it != lst.end() && *it == q)
            std::cout << std::distance(lst.begin(), it) + 1 << spc;
        else
            std::cout << -1 << spc;
    }
}
signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int t = 1;
    // std::cin >> t;
    while (t--) solve();
    return 0;
}