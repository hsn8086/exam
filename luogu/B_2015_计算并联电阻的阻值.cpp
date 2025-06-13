#include <bits/stdc++.h>

using i64 = long long;

int main() {
    double r1, r2;
    std::cin >> r1 >> r2;
    printf("%.2lf", 1 / (1 / r1 + 1 / r2));
    // std::cout << std::setprecision(9) << a / b << std::endl;
    return 0;
}