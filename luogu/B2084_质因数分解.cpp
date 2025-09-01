#include <bits/stdc++.h>

signed main() {
    int n;
    std::cin >> n;
    for (int i = 2; i <= sqrt(n) + 2; i++)
        if (n % i == 0) {
            std::cout << n / i;
            break;
        }
    return 0;
}