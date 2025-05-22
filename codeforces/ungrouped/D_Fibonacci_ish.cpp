
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.1,sse4.2,sse4a,abm,avx,avx2,avx512f,tune=native")
#pragma GCC optimize("inline")
#include <algorithm>
#include <iostream>
#include <unordered_map>

#define endl "\n"

using namespace std;

const int MAXN = 1010; // 根据题目约束调整大小
int a[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    unordered_map<int, int> a_cnt;
    for (int i = 0; i < n; ++i) {
        a_cnt[a[i]]++;
    }

    int max_cnt = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            
            int u = a[i];
            int v = a[j];
            
            // 检查初始元素是否足够
            if (a_cnt[u] < 1 || a_cnt[v] < 1) continue;
            if (u == v && a_cnt[u] < 2) continue;
            
            auto cnt_cpy = a_cnt;
            cnt_cpy[u]--;
            cnt_cpy[v]--;
            
            int cnt = 0;
            while (true) {
                int sum = u + v;
                if (cnt_cpy[sum] < 1) break;
                
                cnt_cpy[sum]--;
                u = v;
                v = sum;
                cnt++;
            }
            
            max_cnt = max(max_cnt, cnt);
        }
    }
    
    cout << (max_cnt + 2) << endl;
    return 0;
}