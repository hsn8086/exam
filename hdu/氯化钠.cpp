#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using i64 = long long; 

int main() {
    std::ios::sync_with_stdio(false); 
    std::cin.tie(nullptr);            

    int t;
    std::cin >> t;

    while (t--) {
        i64 n, k;
        std::cin >> n >> k;

        std::vector<i64> a(n);
        for (i64 i = 0; i < n; i++) {
            std::cin >> a[i];
        }

        
        std::priority_queue<i64, std::vector<i64>, std::greater<i64>> q;

        
        for (i64 i = 0; i < k; i++) {
            q.push(0);
        }

        
        for (i64 val : a) {
            i64 doubled = 2 * val;
            q.push(doubled);
            q.pop(); 
        }

        
        for (i64 i = 0; i < n; i++) {
            i64 v = a[i];
            i64 j = i - 1;
            while (j >= 0 && v <= a[j]) {
                i64 sum = v + a[j];
                q.push(sum);
                q.pop(); 
                j--;
            }
        }

        
        std::reverse(a.begin(), a.end());
        for (i64 i = 0; i < n; i++) {
            i64 v = a[i];
            i64 j = i - 1;
            while (j >= 0 && v <= a[j]) {
                i64 sum = v + a[j];
                q.push(sum);
                q.pop(); 
                j--;
            }
        }

        
        std::cout << q.top() << "\n";
    }

    return 0;
}