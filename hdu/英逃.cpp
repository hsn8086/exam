#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;

class SparseTable {
private:
    vector<vector<i64>> st;
    vector<i64> log;
    i64 n;
    i64 k;
    function<i64(i64, i64)> func;

public:
    SparseTable(const vector<i64>& arr, function<i64(i64, i64)> f = [](i64 a, i64 b) { return min(a, b); }) 
        : func(f), n(arr.size()) {
        log.resize(n + 1);
        for (i64 i = 2; i <= n; ++i) {
            log[i] = log[i / 2] + 1;
        }
        k = log[n];
        st.resize(k + 1, vector<i64>(n));
        st[0] = arr;
        for (i64 j = 1; j <= k; ++j) {
            for (i64 i = 0; i + (1 << j) <= n; ++i) {
                st[j][i] = func(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
            }
        }
    }

    i64 query(i64 left, i64 right) const {
        i64 j = log[right - left + 1];
        return func(st[j][left], st[j][right - (1 << j) + 1]);
    }
};

i64 clac(const vector<i64>& a, const vector<i64>& prefix, const SparseTable& st, i64 l, i64 r) {
    i64 max_ = st.query(l - 1, r - 1);
    i64 red = prefix[min(r, (i64)prefix.size() - 1)] - prefix[max(l - 2, (i64)0)];

    if (r < (i64)a.size()) {
        red -= abs(a[r] - max_);
    }
    if (l - 2 >= 0) {
        red -= abs(a[l - 2] - max_);
    }
    return red;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    i64 t;
    cin >> t;
    while (t--) {
        i64 n, x;
        cin >> n >> x;
        vector<i64> a(n);
        for (i64 i = 0; i < n; ++i) {
            cin >> a[i];
        }
        vector<i64> prefix = {0};
        i64 init = 0;
        for (i64 i = 0; i < n - 1; ++i) {
            init += abs(a[i] - a[i + 1]);
            prefix.push_back(init);
        }
        i64 diff = init - x;
        if (diff <= 0) {
            cout << 0 << '\n';
            continue;
        }
        SparseTable st(a, [](i64 a, i64 b) { return max(a, b); });
        i64 min_d = numeric_limits<i64>::max();
        for (i64 i = 0; i < n - 1; ++i) {
            i64 l = i + 1;
            i64 r = n;
            while (l < r) {
                i64 mid = (l + r) / 2;
                if (clac(a, prefix, st, i + 1, mid) < diff) {
                    l = mid + 1;
                } else {
                    r = mid;
                    min_d = min(min_d, r - i);
                }
            }
            if (clac(a, prefix, st, i + 1, n) >= diff) {
                min_d = min(min_d, n - i);
            }
        }
        cout << min_d << '\n';
    }

    return 0;
}