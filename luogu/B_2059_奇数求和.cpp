#include <bits/stdc++.h>

signed main() {
    int n, m, sum = 0;
    std::cin >> n >> m;
    for (int i = n; i <= m; i++)
        if (i & 1) sum += i;
    std::cout << sum;
    return 0;
}