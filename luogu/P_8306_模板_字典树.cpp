#include <bits/stdc++.h>
#include <iostream>
#define endl '\n'
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;
struct Trie {
    int next[(int)3e6][128], cnt[(int)3e6], ptr = 0;
    void clear() {
        for (int i = 0; i <= ptr; ++i) {
            std::fill(next[i], next[i] + 128, 0);
            cnt[i] = 0;
        }
        ptr = 0;
    }
    void insert(const std::string &s) {
        int node = 0;
        for (char c : s) {
            int idx = c;
            if (!next[node][idx]) next[node][idx] = ++ptr;
            node = next[node][idx];
            cnt[node]++;
        }
    }

    int count(const std::string &s) const {
        int node = 0;
        for (char c : s) {
            int idx = c;
            if (!next[node][idx]) return 0;
            node = next[node][idx];
        }
        return cnt[node];
    }
};
Trie trie;
void solve() {
    int n, q;
    trie.clear();
    std::cin >> n >> q;
    std::string s;
    while (n--) {
        std::cin >> s;
        trie.insert(s);
    }
    while (q--) {
        std::cin >> s;
        std::cout << trie.count(s) << endl;
    }
}
signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int t = 0;
    std::cin >> t;
    while (t--) solve();
    return 0;
}