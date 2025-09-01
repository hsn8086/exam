#include <bits/stdc++.h>
#define ndl '\n'
using i64 = int64_t;
constexpr std::array<int, 211> get_prefix() {
    std::array<int, 211> prefix{};
    prefix[0] = 0;
    for (int i = 1; i < 211; ++i) {
        if (i % 2 and i % 3 and i % 5 and i % 7)
            prefix[i] = prefix[i - 1];
        else
            prefix[i] = prefix[i - 1] + 1;
    }
    return prefix;
}
constexpr auto prefix = get_prefix();

inline i64 check(i64 x) {
    return (x / 210) * prefix.back() + prefix[x % 210];
}

void solve() {
    i64 l, r;
    std::cin >> l >> r;
    std::cout << r - l + 1 - (check(r) - check(l - 1)) << ndl;
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