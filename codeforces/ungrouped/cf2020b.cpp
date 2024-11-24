#include <cmath>
#include <iostream>

using namespace std;
int sqrt_s(double x)
int main() {
    int numOfTC;
    cin >> numOfTC;
    for (int i = 0; i < numOfTC; i++) {
        long long int k;
        cin >> k;
        cout << k + (long long int)ceil((sqrt_s((1 + 4.0 * k)) - 1.0) / 2.0) << endl;
    }
    return 0;
}