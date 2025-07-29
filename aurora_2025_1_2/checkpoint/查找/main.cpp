#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        int result = n; // Default to n if no element >= k is found
        for (int i = 0; i < n; ++i) {
            if (a[i] >= k) {
                result = i + 1;
                break;
            }
        }
        cout << result << endl;
    }
    return 0;
}