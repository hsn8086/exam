#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;
using i64 = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        
        vector<int> a(n), b(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        for (int i = 0; i < n; ++i) cin >> b[i];
        
        i64 last = 0;
        i64 sum = 0;
        i64 cnt = 0;
        vector<i64> lst;
        
        for (int i = 0; i < n; ++i) {
            i64 current = a[i] + b[i];
            if (last != current) {
                lst.push_back(sum * cnt);
                sum = 0;
                last = current;
                cnt = 0;
            }
            sum += a[i];
            cnt += 1;
        }
        lst.push_back(sum * cnt);
        
        i64 max_val = *max_element(lst.begin(), lst.end());
        cout << max_val << '\n';
    }

    return 0;
}