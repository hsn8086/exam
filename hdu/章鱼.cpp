#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<vector<int>> g;
vector<ll> ans;
vector<int> sz;
vector<ll> dp;

void dfs(int u, int p) {
    sz[u] = 1;
    for (int v : g[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            dp[u] += (ll)sz[v] * sz[v];
        }
    }
}

void dfs_reroot(int u, int p, int n) {
    ll sum = 0;
    for (int v : g[u]) {
        if (v == p) continue;
        sum += (ll)sz[v] * sz[v];
    }
    ans[u] += (ll)sz[u] * sz[u] - sum;
    ans[u] = ans[u] * n + (ll)sz[u] * n;

    for (int v : g[u]) {
        if (v == p) continue;
        ll old_sz_u = sz[u];
        ll old_sz_v = sz[v];
        ll old_dp_u = dp[u];
        ll old_dp_v = dp[v];

        sz[u] = n - sz[v];
        dp[u] = dp[u] - (ll)old_sz_v * old_sz_v + (ll)(n - old_sz_v) * (n - old_sz_v);
        sz[v] = n;
        dp[v] += (ll)sz[u] * sz[u] - (ll)old_sz_u * old_sz_u;

        dfs_reroot(v, u, n);

        sz[u] = old_sz_u;
        sz[v] = old_sz_v;
        dp[u] = old_dp_u;
        dp[v] = old_dp_v;
    }
}

void solve() {
    int n;
    cin >> n;
    g.assign(n + 1, {});
    ans.assign(n + 1, 0);
    sz.assign(n + 1, 0);
    dp.assign(n + 1, 0);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    dfs(1, 0);
    dfs_reroot(1, 0, n);

    for (int i = 1; i <= n; i++) {
        ans[i] = (ans[i] + (ll)n * (n + 1)) / 2;
    }

    for (int i = 1; i <= n; i++) {
        cout << ans[i] << " ";
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
