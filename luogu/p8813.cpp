#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (a == 1) {
        cout << 1;
        return 0;
    }
    long long res = 1;
    while (b-- && res <= 1e9) {
        res *= a;
    }
    if (res > 1e9) {
        cout << -1;
        return 0;
    }
    cout << res;
    return 0;
}