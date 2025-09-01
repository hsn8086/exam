#include <bits/stdc++.h>
#include <iostream>
#include <iterator>
#include <map>
#include <vector>
// #define endl std::endl
#define endl '\n'
#define elif else if
#define in :
#define cin  std::cin
#define cout std::cout

using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;

void solve() {
    int n, q;
    cin >> n >> q;
    std::vector<int> a;
    std::map<int, int> cnt;
    int threshold = n - std::ceil((n - 1) / 2.0);
    while (n--) {
        int x;
        cin >> x;
        a.push_back(x);
        cnt[x]++;
    }
    
    int sum = 0, div = 0;

    for (auto [i, freq] in cnt) {
        sum += freq;
        if (sum <= threshold)
            div = i;
        else {
            sum -= freq;
            break;
        }
    }
    while (q--) {
        int i, d;
        cin >> i >> d;
        int v = a[i - 1];
        a[i - 1] += d;
        int target = a[i - 1];
        cnt[v]--;
        cnt[target]++;

        if (v <= div and target > div) sum -= 1;
        elif (v > div and target <= div) sum += 1;

        auto it = cnt.lower_bound(div);
        it++;
        int tmp = 3;
        while (tmp--) {
            if (it != cnt.begin()) {
                it--;
                sum -= it->second;
            } else {
                it = cnt.begin();
                break;
            }
        }
        for (auto jt = it; jt != cnt.end() && jt != std::next(it, 6); jt++) {
            auto freq = jt->second;
            if (freq <= 0) continue;
            sum += freq;
            if (sum <= threshold)
                div = jt->first;
            else {
                sum -= freq;
                break;
            }
        }
        if (cnt[v] == 0) {
            cnt.erase(v);
        }
        cout << sum << endl;
    }
}
signed main() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}