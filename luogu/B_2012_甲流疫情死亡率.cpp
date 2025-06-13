#include <bits/stdc++.h>

using i64 = long long;

int main() {
    double a, b;
    std::cin >> a >> b;
    printf("%.3f%%", 100 * b / a);
    // std::cout << std::setprecision(9) << a / b << std::endl;
    return 0;
}