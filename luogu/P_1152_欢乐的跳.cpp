#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n), d(n - 1);
    for (auto &i : a) std::cin >> i;
    for (int i = 0; i < n - 1; i++) {
        d[i] = abs(a[i + 1] - a[i]);
    }
    std::sort(d.begin(), d.end());
    for (int i = 0; i < n - 1; i++) {
        if (d[i] != i + 1) {
            std::cout << "Not jolly";
            goto out;
            break;
        }
    }
    std::cout << "Jolly";
out:
    return 0;
}