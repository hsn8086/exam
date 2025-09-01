#include <bits/stdc++.h>
#include <iostream>
#include <numeric>
#define endl '\n'
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;

void solve() {
    int a, b;
    std::cin >> a >> b;
    std::cout << std::gcd(a, b) << " " << std::lcm(a, b) << endl;
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