#include <bits/stdc++.h>
using i64 = int64_t;

i64 fastPow(i64 base, int power, i64 mod) {
    base %= mod;
    i64 ans = 1;
    while (power) {
        if (power & 1) ans = (ans * base) % mod;
        base = (base * base) % mod;
        power >>= 1;
    }
    return ans;
}

signed main() {
    int a, b, p;
    std::cin >> a >> b >> p;
    printf("%d^%d mod %d=%ld", a, b, p, fastPow(a, b, p));
    return 0;
}