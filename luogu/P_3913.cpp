#include <bits/stdc++.h>
#include <iostream>
#include <set>
#include <unordered_set>
#define endl '\n'
constexpr char spc = ' ';
#define forrange(i, start, end) for (const auto i : std::ranges::iota_view{start, end})
using i64 = int64_t;
using u64 = uint64_t;
using i128 = __int128_t;
using u128 = __uint128_t;
using f128 = __float128;

void solve() {
    std::unordered_set<int> a;
    std::unordered_set<int> b;
    int n, k, x, y;
    std::cin >> n >> k;
    forrange(i, 0, k) {
        std::cin >> x >> y;
        a.insert(x);
        b.insert(y);
    }
    std::cout << (i64)n * (i64)n - (i64)(n - a.size()) * (i64)(n - b.size()) << endl;
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