#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cstdint>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        unordered_map<int64_t, int> act;
        unordered_set<int64_t> ans_act;
        int last_z = 0;
        int n;
        cin >> n;
        vector<int64_t> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        vector<int> pre(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pre[i] = ans_act.size();
            if (a[i] == 0) {
                last_z = i;
            } else if (act.find(a[i]) == act.end()) {
                act[a[i]] = i;
            } else if (last_z > act[a[i]]) {
                ans_act.insert(a[i]);
            }
        }

        vector<int64_t> rst(1e6 + 10, 0);
        for (int i = 0; i < n; ++i) {
            if (a[i] != 0) {
                rst[a[i]] = max(rst[a[i]], static_cast<int64_t>(pre[i]));
            }
        }

        int64_t sum = 0;
        for (const auto& val : rst) {
            sum += val;
        }

        cout << sum << '\n';
    }

    return 0;
}