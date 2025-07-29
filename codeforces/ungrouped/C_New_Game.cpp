#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int ntc;
    cin >> ntc;
    for (int tc = 0; tc < ntc; ++tc) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        unordered_map<int, int> c;
        for (int num : a) {
            c[num]++;
        }
        int min_key = INT_MAX;
        int max_key = INT_MIN;
        for (auto& pair : c) {
            if (pair.first < min_key) min_key = pair.first;
            if (pair.first > max_key) max_key = pair.first;
        }
        vector<int> temp = {0};
        int ans = 0;
        for (int i = min_key; i <= max_key + 1; ++i) {
            if (c.count(i)) {
                temp.push_back(temp.back() + c[i]);
            } else {
                if (temp.size() <= k) {
                    ans = max(ans, temp.back() - temp[0]);
                } else {
                    for (int j = 0; j <= temp.size() - k; ++j) {
                        ans = max(ans, temp[j + k] - temp[j]);
                    }
                }
                temp = {0};
            }
        }
        cout << ans << endl;
    }
    return 0;
}