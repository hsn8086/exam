#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;
using i64 = long long;

int main() {
    i64 n;
    cin >> n;
    i64 cnt = 0;
    i64 max_ = sqrt(n) + 10;
    
    for (i64 k = 1; k <= max_; k += 2) {
        i64 m = n / (k * k);
        if (m >= 2) {
            cnt += bitset<64>(m).size() - __builtin_clzll(m) - 1;
        }
    }
    
    cout << cnt << endl;
    return 0;
}