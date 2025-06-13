#include <bits/stdc++.h>

using i64 = long long;

int main() {
    double a, pi = 3.14159;
    std::cin >> a;
    printf("%.4lf %.4lf %.4lf", a * 2, 2 * pi * a, pi * a * a);
    // std::cout << std::setprecision(9) << a / b << std::endl;
    return 0;
}