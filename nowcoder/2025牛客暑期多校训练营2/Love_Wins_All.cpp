#include <bits/stdc++.h>
using namespace std;
using ll = long long;
static const int MOD = 998244353;

int add(int a, int b) { a += b; if (a >= MOD) a -= MOD; return a; }
int mul(ll a, ll b) { return int((a * b) % MOD); }
int modpow(int a, ll e=MOD-2) {
    ll r = 1, x = a;
    while (e) {
        if (e & 1) r = (r * x) % MOD;
        x = (x * x) % MOD;
        e >>= 1;
    }
    return int(r);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    vector<int> a;
    while (T--) {
        int n;
        cin >> n;
        a.resize(n+1);
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }

        vector<char> vis(n+1, 0);
        vector<int> oddLens, evenLens;
        // 找环
        for (int i = 1; i <= n; i++) {
            if (!vis[i]) {
                int u = i, len = 0;
                while (!vis[u]) {
                    vis[u] = 1;
                    u = a[u];
                    len++;
                }
                if (len & 1) oddLens.push_back(len);
                else        evenLens.push_back(len);
            }
        }

        int me = evenLens.size();
        int mo = oddLens.size();
        // 2^me
        int pow2_me = modpow(2, me);

        ll ans = 0;

        // 情况1：两个未婚在同一个偶环，必须 mo==0
        if (mo == 0) {
            // sum f(L,2)
            ll sumF2 = 0;
            for (int L : evenLens) {
                // floor(L/4)*L
                ll term = ll(L/4) * L % MOD;
                // 如果 L%4==2，加 L/2
                if (L % 4 == 2) term = (term + L/2) % MOD;
                sumF2 = (sumF2 + term) % MOD;
            }
            // 2^{me-1} * sumF2
            int inv2 = (MOD + 1) / 2;
            int coef = mul(pow2_me, inv2);
            ans = (ans + coef * sumF2) % MOD;
        }

        // 情况2：在两个不同奇环里恰各选 1 个，必须 mo==2
        if (mo == 2) {
            ll L1 = oddLens[0], L2 = oddLens[1];
            ll term = (L1 % MOD) * (L2 % MOD) % MOD;
            term = term * pow2_me % MOD;
            ans = (ans + term) % MOD;
        }

        cout << ans << "\n";
    }
    return 0;
}
