#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

int main() {
    int num_of_tc;
    std::cin >> num_of_tc;

    while (num_of_tc--) {
        long long n;
        std::cin >> n;

        std::vector<long long> a(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> a[i];
        }

        if (n % 2 == 1) {
            long long minn = std::numeric_limits<long long>::max(); // Use max instead of hardcoded value
            for (int j = 0; j < n; j++) {
                std::vector<long long> b = a;
                b.erase(b.begin() + j);
                long long maxn = 0;
                for (int i = 0; i < n - 2; i += 2) {
                    long long c = b[i + 1] - b[i];
                    maxn = std::max(maxn, c);
                }
                minn = std::min(minn, maxn);
            }
            if (minn==0) {
                std::cout << 1 << std::endl;
            }else {
                std::cout << minn << std::endl;
            }
            

        } else {
            long long max_diff = 0; // Changed to long long to avoid overflow
            for (int i = 1; i < n; i+=2) {
                max_diff = std::max(max_diff, a[i] - a[i - 1]);
            }
            std::cout << max_diff << std::endl;
        }
    }

    return 0;
}
