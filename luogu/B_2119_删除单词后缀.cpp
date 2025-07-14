#include <bits/stdc++.h>
#include <iostream>
#include <string>
#define endl '\n'
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;

void solve() {
    std::string s;
    std::cin >> s;
    int length = s.length();
    if (length >= 2 &&
        ("er" == s.substr(length - 2, 2) || "ly" == s.substr(length - 2, 2))) {
        std::cout << s.substr(0, length - 2) << endl;
    } else if (length >= 3 && "ing" == s.substr(length - 3, 3)) {
        std::cout << s.substr(0, length - 3) << endl;
    } else {
        std::cout << s << endl;
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