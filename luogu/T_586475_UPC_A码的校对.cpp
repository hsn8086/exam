#include <bits/stdc++.h>
#define ndl "\n"

void solve() {
    std::string s;
    std::cin >> s;
    std::pmr::vector<int> a;
    for (const char c : s)
        if (c >= 48) a.push_back(c - 48);
    int code = a.back();
    a.pop_back();

    int odd = 0, even = 0, i = 0;
    for (const int e : a)
        if (++i & 1)
            odd += e;
        else
            even += e;

    if ((10 - (odd * 3 + even) % 10) % 10 == code)
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