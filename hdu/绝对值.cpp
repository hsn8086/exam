#include <iostream>
#include <vector>
#include <cstdlib> 

using i64 = long long; 

int main() {
    int n;
    std::cin >> n;

    i64 count = 0;
    std::vector<i64> a_pfx = {0}; 
    std::vector<i64> a_ppfx = {0}; 

    for (int i = 0; i < n; i++) {
        i64 val;
        std::cin >> val;

        a_pfx.push_back(a_pfx.back() + std::abs(val));
        a_ppfx.push_back(a_ppfx.back() + a_pfx.back());
    }
    std::cout << a_ppfx.back() << std::endl;

    return 0;
}