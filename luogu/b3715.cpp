#include <iostream>
using namespace std;
using i64 = long long;
int main() {
    int ntc;
    cin >> ntc;
    while (ntc--) {
        i64 n;
        cin >> n;

        if (n < 2) {
            return 0;
        }

        for (i64 i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                n = n / i;
                cout << i;
                if (n != 1)
                    cout << " ";
            }
        }
        if (n != 1) {
            cout << n;
        }
        cout << endl;
    }

    return 0;
}