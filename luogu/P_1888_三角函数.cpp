#include <bits/stdc++.h>

int main() {
    std::vector<int> a(3);
    for (auto &i : a) std::cin >> i;
    std::sort(a.begin(), a.end());
    int g = std::gcd(a[0], a[2]);
    std::cout << a[0] / g << "/" << a[2] / g;
    return 0;
}