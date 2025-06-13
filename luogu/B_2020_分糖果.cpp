#include <bits/stdc++.h>

using i64 = long long;

int main() {
    std::vector<int> a(5);
    int cnt = 0;
    for (auto &i : a) std::cin >> i;
    for (int i = 0; i < 5; i++) {
        a[(i + 4) % 5] += a[i] / 3;
        a[(i + 6) % 5] += a[i] / 3;
        cnt += a[i] % 3;
        a[i] = a[i] / 3;
    }
    for (auto &i : a) std::cout << i << " ";
    std::cout << std::endl << cnt << std::endl;
    return 0;
}