#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int64_t> r, b;
        vector<int64_t> values(n);
        for (auto& v : values) {
            cin >> v;
        }
        string types;
        cin >> types;
        for (int i = 0; i < n; ++i) {
            if (types[i] == 'R') {
                r.push_back(values[i]);
            } else {
                b.push_back(values[i]);
            }
        }
        sort(r.rbegin(), r.rend());
        sort(b.rbegin(), b.rend());
        
        int64_t sum = 0;
        if (r.size() > b.size()) {
            int i = b.size();
            for (int j = 0; j <= i; ++j) {
                if (j < r.size()) sum += r[j];
            }
            for (int j = 0; j < i; ++j) {
                if (j < b.size()) sum += b[j];
            }
        } else {
            int i = r.size();
            for (int j = 0; j < i; ++j) {
                if (j < r.size()) sum += r[j];
            }
            for (int j = 0; j < i; ++j) {
                if (j < b.size()) sum += b[j];
            }
        }
        cout << sum << '\n';
    }
    
    return 0;
}