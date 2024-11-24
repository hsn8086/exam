
#include <iostream>
#include <algorithm>
using namespace std;

bool is_divisor(long long a, long long b) {
    return b != 0 && a % b == 0;
}

int main() {
    int n;
    cin >> n;
    
    while (n--) {
        long long x, m;
        cin >> x >> m;
        long long count = 0;
        
        for (long long y = 1; y <= min(m, x); y++) {
            long long xor_val = x ^ y;
            
            if (is_divisor(xor_val, x) || is_divisor(xor_val, y)) {
                count++;
            }
        }

        long long xor_val = x;
        while (xor_val <= m * 2) {
            xor_val += x;
            long long y = x ^ xor_val;
            
            if (y <= m && y != 0) {
                count++;
            }
        }
        
        cout << count << endl;
    }
    
    return 0;
}