#include <iostream>
#include <map>
#include <vector>
#define i64 long long
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<i64> prefix_sum(n + 100);
        for (int i = 0; i < n; ++i) {
            int tmp;
            cin >> tmp;
            prefix_sum[i + 1] = prefix_sum[i] + tmp;
        }

        vector<i64> dp(n + 100);
        map<i64, int> seen;
        seen[0] = 0;

        for (int i = 1; i <= n; ++i) {

            if (seen.find(prefix_sum[i]) != seen.end()) {
                int last = seen[prefix_sum[i]];
                dp[i] = max(dp[i - 1], dp[last] + 1);
            } else {
                dp[i] = dp[i - 1];
            }

            seen[prefix_sum[i]] = i;
        }
        cout << dp[n] << endl;
    }

    return 0;
}
