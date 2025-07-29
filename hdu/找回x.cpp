#include <iostream>

using i64 = long long; 

int main() {
    std::ios::sync_with_stdio(0),std::cin.tie(0),std::cout.tie(0);
    int t;
    std::cin >> t;

    while (t--) {
        i64 n;
        std::cin >> n;

        i64 a = 0, b = 0, c = 0;

        
        for (i64 i = 0; i < n; i++) {
            i64 val;
            std::cin >> val;
            a += val;
        }

        
        for (i64 i = 0; i < n; i++) {
            i64 val;
            std::cin >> val;
            b += val;
        }

        
        for (i64 i = 0; i < n; i++) {
            i64 val;
            std::cin >> val;
            c += val;
        }

        
        i64 result = (c - b) / a;
        std::cout << result << "\n";
    }

    return 0;
}