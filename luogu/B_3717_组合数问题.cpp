#include <array>
#include <bits/stdc++.h>
#include <iostream>
constexpr char endl = '\n';
constexpr char spc = ' ';
#define forrange(i, start, end) for (const auto i : std::ranges::iota_view{start, end})
using i64 = int64_t;
using u64 = uint64_t;
using i128 = __int128_t;
using u128 = __uint128_t;
using f128 = __float128;
constexpr int mod = 998244353;
template <const int MOD> struct ModInt {
    int x;
    ModInt(int x = 0) : x(x % MOD) {
        if (x < 0) x += MOD;
    }
    ModInt operator+(ModInt o) const { return ModInt(x + o.x); }
    ModInt operator-(ModInt o) const { return ModInt(x - o.x); }
    ModInt operator*(ModInt o) const { return ModInt(1LL * x * o.x % MOD); }
    ModInt operator/(ModInt o) const { return *this * o.inv(); }
    ModInt inv() const { return pow(MOD - 2); }
    ModInt pow(long long e) const {
        ModInt ans = 1, b = *this;
        while (e) {
            if (e & 1) ans = ans * b;
            b = b * b;
            e >>= 1;
        }
        return ans;
    }
};


using MI = ModInt<mod>;
std::array<MI, (int)5e6 + 1> fact;
void solve() {
    int n, m, a, b;
    std::cin >> n >> m;

    MI now = 1;
    fact[0] = now;
    forrange(i, 1, (int)5e6 + 1) {
        now = now * MI(i);
        fact[i] = now;
    }
    int ans = 0;
    forrange(_, 0, n) {
        std::cin >> a >> b;
        // std::cout<<fact[a].x<<spc<<fact[a - b].x<<spc<<fact[b].x<<endl;
        ans ^= ((fact[a] / fact[a - b]) / fact[b]).x;
    }
    std::cout << ans;
}
signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int t = 1;
    // std::cin >> t;
    while (t--) solve();
    return 0;
}