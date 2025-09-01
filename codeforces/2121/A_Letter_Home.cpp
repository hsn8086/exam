#include <bits/stdc++.h>
#define ndl '\n'
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;

void solve() {
    int n, s;
    std::cin >> n >> s;
    std::vector<int> a(n);
    for (auto &e : a) std::cin >> e;
    for (auto &e : a) e -= s;

    std::vector<bool> sign = {};
    for (const auto e : a) sign.push_back(std::signbit(e));
    
    if (std::all_of(sign.begin(), sign.end(), [](bool b) { return b; }) or
        std::none_of(sign.begin(), sign.end(), [](bool b) { return b; })) {
        int ans = -1;
        for (const auto e : a) ans = std::max(ans, abs(e));
        std::cout << ans << ndl;
    } else {
        int min = INT_MAX, max = INT_MIN;

        for (const auto e : a) {
            min = std::min(e, min);
            max = std::max(e, max);
        }

        std::cout << std::min(-min, max) * 2 + std::max(-min, max) << ndl;
    }
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