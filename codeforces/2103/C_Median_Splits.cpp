#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while(T--){
        int n;
        ll k;
        cin >> n >> k;
        vector<ll>a(n);
        for(auto &x:a) cin >> x;

        // 特判 n == 3
        if(n==3){
            auto b=a;
            sort(b.begin(), b.end());
            cout << (b[1] <= k ? "YES\n" : "NO\n");
            continue;
        }

        // small[i]=1 if a[i]<=k
        vector<int> small(n);
        for(int i=0;i<n;i++) small[i] = (a[i]<=k);

        // 前缀和 pre[i], P[i] = 2*pre[i] - i
        vector<int> pre(n+1,0), P(n+1,0);
        for(int i=1;i<=n;i++){
            pre[i] = pre[i-1] + small[i-1];
            P[i] = 2*pre[i] - i;
        }

        // 后缀好坏 h[i]=1 if a[i..n] 好段
        vector<bool> h(n+2,false);
        for(int i=1;i<=n;i++){
            int m = n - i + 1;
            int cnt = pre[n] - pre[i-1];
            int val = 2*cnt - m;
            if(val >= m%2) h[i] = true;
        }

        // ------- 跳过第二段：只看 S1 & S3 -------
        vector<bool> f1(n+1,false);
        for(int i=1;i<=n;i++){
            // 前缀 [1..i] 好段判定
            if(P[i] >= (i%2)) f1[i] = true;
        }
        bool skip2 = false;
        // 枚举 j = r+1 从 3..n，看后缀 [j..n] 好，
        // 并在 j-2 之前寻找任一 f1[l]
        bool any_f1 = false;
        for(int j=3;j<=n;j++){
            if(f1[j-2]) any_f1 = true;
            if(h[j] && any_f1){
                skip2 = true;
                break;
            }
        }

        // ------- 跳过第一段：只看 S2 & S3 -------
        auto solve_skip1 = [&](const vector<ll>& a_, ll k_){
            int N = a_.size();
            // small, pre, P 同上
            vector<int> sm(N), pr(N+1,0), PP(N+1,0);
            for(int i=0;i<N;i++) sm[i] = (a_[i]<=k_);
            for(int i=1;i<=N;i++){
                pr[i] = pr[i-1] + sm[i-1];
                PP[i] = 2*pr[i] - i;
            }
            // 后缀好坏 h2[i]
            vector<bool> h2(N+2,false);
            for(int i=1;i<=N;i++){
                int m = N - i + 1;
                int cnt = pr[N] - pr[i-1];
                int val = 2*cnt - m;
                if(val >= m%2) h2[i] = true;
            }
            // 维护到 t=r-1 的 PP[t] 最小值，按 parity 分两组
            const ll INF = 1e18;
            ll mn[2] = {INF, INF};
            // 枚举 r 从 2..N-1
            for(int r=2;r< N;r++){
                int t = r-1;
                mn[t%2] = min(mn[t%2], (ll)PP[t]);
                ll prr = PP[r];
                bool ok = false;
                // 如果存在同 parity 的 t: mn[p]==最小 PP[t] ≤ prr
                if(mn[r%2] <= prr) ok = true;
                // 如果存在异 parity 的 t: mn[1-p] ≤ prr - 1
                if(mn[1-(r%2)] <= prr - 1) ok = true;
                if(ok && h2[r+1]) {
                    return true;
                }
            }
            return false;
        };

        // 正序跳过第一段
        bool skip1 = solve_skip1(a, k);
        // 反序跳过第三段
        auto a_rev = a;
        reverse(a_rev.begin(), a_rev.end());
        bool skip3 = solve_skip1(a_rev, k);

        cout << ((skip1||skip2||skip3) ? "YES\n" : "NO\n");
    }

    return 0;
}
