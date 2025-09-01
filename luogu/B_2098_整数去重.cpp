#include <bits/stdc++.h>
#define ndl '\n'
#define spc " "

signed main() {
    int n;
    std::cin >> n;
    std::set<int> s;
    for (int i = 0; i < n; i++) {
        int inp;
        std::cin >> inp;
        if (s.contains(inp)) continue;
        s.insert(inp);
        std::cout << inp << spc;
    }
    return 0;
}