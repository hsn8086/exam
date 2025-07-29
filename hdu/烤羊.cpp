#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using i64 = long long;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;
    
    while (t--) {
        i64 k, a, b, c;
        std::cin >> k >> a >> b >> c;
        
        std::vector<i64> lst = {a, b, c};
        i64 max_ = 0;
        
        // Check single elements
        for (i64 num : lst) {
            if (num <= k) {
                max_ = std::max(max_, num);
            }
        }
        
        // Check all pairs
        for (int i = 0; i < 3; ++i) {
            for (int j = i + 1; j < 3; ++j) {
                i64 sum = lst[i] + lst[j];
                if (sum <= k) {
                    max_ = std::max(max_, sum);
                }
            }
        }
        
        // Check all three elements
        i64 total = a + b + c;
        if (total <= k) {
            max_ = std::max(max_, total);
        }
        
        std::cout << k - max_ << '\n';
    }
    
    return 0;
}