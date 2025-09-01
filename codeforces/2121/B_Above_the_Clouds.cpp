#include <bits/stdc++.h>
#define ndl '\n'
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;

void solve() {
    int n;
    std::string s;
    std::cin >> n >> s;
    std::string ss = s.substr(1, n - 2);
    std::set<char> st(ss.begin(), ss.end());
    if (st.size() != ss.size() or st.contains(s.front()) or
        st.contains(s.back()))
        std::cout << "Yes" << ndl;
    else
        std::cout << "No" << ndl;
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