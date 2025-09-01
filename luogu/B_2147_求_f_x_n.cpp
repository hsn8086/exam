#include <bits/stdc++.h>

double f(double x, int n) {
    if (n == 1)
        return sqrtf64(1 + x);
    else
        return sqrtf64(n + f(x, n - 1));
}

signed main() {
    double x;
    int n;
    std::cin >> x >> n;
    std::cout << std::fixed << std::setprecision(2) << f(x, n);
    return 0;
}