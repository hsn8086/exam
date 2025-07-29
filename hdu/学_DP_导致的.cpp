#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int inp_bignum(const string& x) {
    if (x.length() >= 3) {
        return 100;
    } else {
        return stoi(x);
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s, k_raw;
        cin >> s >> k_raw;
        int k = inp_bignum(k_raw);

        set<char> unique_chars(s.begin(), s.end());
        int ls = unique_chars.size();

        if (k >= ls) {
            cout << ls << endl;
        } else {
            string repeated_s;
            for (int i = 0; i < k; ++i) {
                repeated_s += s;
            }

            vector<int> dp(repeated_s.length(), 1);
            for (size_t i = 0; i < repeated_s.length(); ++i) {
                char vi = repeated_s[i];
                for (size_t j = 0; j < i; ++j) {
                    char vj = repeated_s[j];
                    if (vi > vj) {
                        dp[i] = max(dp[i], dp[j] + 1);
                    }
                }
            }

            int max_dp = *max_element(dp.begin(), dp.end());
            cout << max_dp << endl;
        }
    }
    return 0;
}