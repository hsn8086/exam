#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void dfs(const vector<vector<int>>& e, vector<bool>& tag, int i) {
    stack<int> stk;
    stk.push(i);
    
    while (!stk.empty()) {
        int current = stk.top();
        stk.pop();
        
        if (tag[current]) {
            continue;
        }
        
        tag[current] = true;
        
        for (int j : e[current]) {
            if (!tag[j]) {
                stk.push(j);
            }
        }
    }
}

int main() {
    std::ios::sync_with_stdio(0);
  std::cin.tie(0);
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        
        vector<vector<int>> e(n);
        for (int i = 0; i < n; ++i) {
            if (i + a[i] < n) {
                e[i].push_back(i + a[i]);
                e[i + a[i]].push_back(i);
            }
            if (i - a[i] >= 0) {
                e[i].push_back(i - a[i]);
                e[i - a[i]].push_back(i);
            }
        }
        
        vector<bool> tag(n, false);
        int cnt = 0;
        
        for (int i = 0; i < n; ++i) {
            if (!tag[i]) {
                dfs(e, tag, i);
                cnt++;
            }
        }
        
        cout << cnt - 1 << endl;
    }
    
    return 0;
}