#include <iostream>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    std::cin >> t;
    while (t--) {
        int n;
        std::cin >> n;
        long long mod = 1e9 + 7;
        long long half = n / 2;
        long long result = (half*(half+1)) % mod;
        std::cout << result << "\n";
    }
    return 0;
}
