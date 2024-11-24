#include <algorithm>
#include <iostream>
using namespace std;

inline bool is_divisor(long long a, long long b) { 
    return b != 0 && a % b == 0; 
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    while (n--) {
        long long x, m;
        cin >> x >> m;
        int count = 0;
        
        long long upper = min(m, x * 2);
        

        for (long long y = 1; y <= upper; y++) {
            if (y == x) continue;
            
            long long xor_val = x ^ y;
            if (xor_val > x && xor_val > y) continue; 
            
            if (is_divisor(x, xor_val) || is_divisor(y, xor_val)) {
                count++;
            }
        }
        
        cout << count << '\n'; 
    }
    
    return 0;
}