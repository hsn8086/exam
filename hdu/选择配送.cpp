#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    i64 t;
    cin >> t;

    while (t--) {
        i64 n, m;
        cin >> n >> m;

        i64 left = LLONG_MAX, right = 0;

        for (i64 i = 0; i < n; ++i) {
            i64 x, y;
            cin >> x >> y;
            i64 sum = x + y;
            left = min(left, sum);
            right = max(right, sum);
        }

        i64 ans = LLONG_MAX;

        for (i64 i = 0; i < m; ++i) {
            i64 x, y;
            cin >> x >> y;
            i64 d = x + y;

            i64 current = max(abs(left - d), abs(right - d));
            ans = min(ans, current);
        }

        cout << ans << endl;
    }

    return 0;
}