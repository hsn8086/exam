#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solve(int n, int m, int k, deque<int>& a, vector<pair<int, int>>& ops) {
    int max_left_offset = 0;
    int max_right_offset = 0;
    int current = 0;
    vector<int> results;

    for (const auto& op : ops) {
        if (op.first == 1) {
            current += op.second;
            max_right_offset = max(current, max_right_offset);
        } else if (op.first == 2) {
            current -= op.second;
            max_left_offset = min(current, max_left_offset);
        } else if (op.first == 3) {
            while (!a.empty() && a.front() + max_left_offset < -k) {
                a.pop_front();
            }
            while (!a.empty() && a.back() + max_right_offset > k) {
                a.pop_back();
            }

            results.push_back(a.size());
        }
    }
    return results;
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    sort(a.begin(), a.end());
    deque<int> d(a.begin(), a.end());

    vector<pair<int, int>> ops(m);
    for (int i = 0; i < m; ++i) {
        int op_type, value;
        cin >> op_type;
        if (op_type != 3) {
            cin >> value;
            ops[i] = {op_type, value};
        } else {
            ops[i] = {op_type, 0}; // Placeholder for operations of type 3
        }
    }

    vector<int> results = solve(n, m, k, d, ops);
    for (int res : results) {
        cout << res << endl;
    }

    return 0;
}
