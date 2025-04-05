#include <iostream>
#include <vector>
#include <numeric> // for std::gcd

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    std::vector<int> lst(n, 1);
    for (int i = 1; i < n; ++i) {
        int sum_ = 0;
        for (int j = 0; j < i; ++j) {
            if (std::gcd(a[i], a[j]) != 1) {
                sum_ += lst[j];
            }
        }
        lst[i] = sum_;
    }

    std::cout << lst[n - 1] << std::endl;
    return 0;
}