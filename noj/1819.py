#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using int64 = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int64 n, h;
    cin >> n >> h;

    vector<int64> diff(n + 2, 0); // Using n+2 to avoid out-of-bounds access
    for (int64 i = 0; i < n; ++i) {
        int64 li, hi;
        cin >> li >> hi;
        diff[li] += 1;
        if (hi + 1 <= n) {
            diff[hi + 1] -= 1;
        }
    }

    vector<int64> lst(n, 0);
    for (int64 i = 0; i < n; ++i) {
        if (i > 0) {
            lst[i] += lst[i - 1];
        }
        lst[i] += diff[i];
    }

    vector<int64> pre(n, 0);
    for (int64 i = 0; i < n; ++i) {
        if (i > 0) {
            pre[i] += pre[i - 1];
        }
        pre[i] += lst[i];
    }

    // Adding a 0 at the beginning of the prefix sum array
    pre.insert(pre.begin(), 0);

    int64 max_ = 0;
    for (int64 i = 0; i <= n - h; ++i) {
        max_ = max(pre[i + h] - pre[i], max_);
    }

    cout << h * n - max_ << endl;

    return 0;
}