#include <bits/stdc++.h>
using namespace std;
using i64 = long long;

const i64 MOD = 1e9 + 7;

i64 mod_pow(i64 base, i64 exp, i64 mod) {
    i64 result = 1;
    while (exp > 0) {
        if (exp % 2 == 1)
            result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

i64 mod_inverse(i64 x, i64 mod) {
    return mod_pow(x, mod - 2, mod);
}

i64 comb(i64 n, i64 k, i64 mod) {
    if (k > n) return 0;
    if (k == 0 || k == n) return 1;
    i64 numerator = 1;
    for (i64 i = 0; i < k; ++i)
        numerator = (numerator * (n - i)) % mod;
    i64 denominator = 1;
    for (i64 i = 1; i <= k; ++i)
        denominator = (denominator * i) % mod;
    return (numerator * mod_inverse(denominator, mod)) % mod;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<i64> a(n);
        for (auto& x : a) cin >> x;

        i64 ans = 0, sum_ = 0;
        for (i64 x : a) {
            ans = (ans + sum_ * x) % MOD;
            sum_ = (sum_ + x) % MOD;
        }

        i64 comb_cnt = 1;
        for (int i = 2; i <= n; ++i) {
            i64 c = comb(i, 2, MOD);
            comb_cnt = (comb_cnt * c) % MOD;
        }

        cout << ans % MOD << ' ' << comb_cnt % MOD << '\n';
    }

    return 0;
}