#include <iostream>
#include <cmath> 
#include <cstdint>
using namespace std;


int64_t cal(int64_t x) {
    x -= 1;
    if (x <= 0) {
        return 0;
    }
    int64_t c = ceil(x / 2.0); 
    int64_t f = floor(x / 2.0);
    return (c + 1) * c / 2 + (f + 1) * f / 2;
}

int main() {
    ios::sync_with_stdio(false); 
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int64_t n, k;
        cin >> n >> k;
        if (k%2==1){
            cout<<0;continue;
        }
        k = k / 2; 
        int64_t l_ = n / k; 
        int64_t a = n % k; 
        int64_t b = k - a;

        
        int64_t result = b * cal(l_) + a * cal(l_ + 1);
        cout << result << '\n';
    }

    return 0;
}