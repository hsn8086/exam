#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <unordered_map>
#include <numeric>
using namespace std;

using i64 = long long;
const i64 MOD = 998244353;

vector<i64> fact;

void precompute_factorials(int max_n) {
    fact.resize(max_n + 1);
    fact[0] = 1;
    for (int i = 1; i <= max_n; i++) {
        fact[i] = fact[i-1] * i % MOD;
    }
}

i64 count(const vector<int>& counts) {
    i64 total = accumulate(counts.begin(), counts.end(), 0);
    i64 denominator = 1;
    for (int cnt : counts) {
        denominator = denominator * fact[cnt] % MOD;
    }
    
    i64 inv_denominator = 1, base = denominator, power = MOD - 2;
    while (power > 0) {
        if (power % 2 == 1) {
            inv_denominator = inv_denominator * base % MOD;
        }
        base = base * base % MOD;
        power /= 2;
    }
    
    return fact[total] * inv_denominator % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    const int MAX_FACT = 1e6;
    precompute_factorials(MAX_FACT);
    
    int t;
    cin >> t;
    
    while (t--) {
        vector<int> a;
        int num;
        while (cin >> num) {
            if (num == 0) continue;
            a.push_back(num);
            if (cin.peek() == '\n') break;
        }
        
        int total = accumulate(a.begin(), a.end(), 0);
        int target = total / 2;
        int n = a.size();
        
        vector<vector<int>> dp(target + 1);
        dp[0] = vector<int>();
        
        for (int num : a) {
            for (int j = target; j >= num; j--) {
                if (!dp[j - num].empty() && dp[j].empty()) {
                    dp[j] = dp[j - num];
                    dp[j].push_back(num);
                }
            }
        }
        
        vector<i64> dp2(target + 1, 0);
        dp2[0] = 1;
        for (int x : a) {
            for (int j = target; j >= x; j--) {
                dp2[j] = (dp2[j] + dp2[j - x]) % MOD;
            }
        }
        
        vector<int> selected;
        for (int j = target; j >= 0; j--) {
            if (!dp[j].empty()) {
                selected = dp[j];
                break;
            }
        }
        
        // Shuffle the selected elements
        random_device rd;
        mt19937 g(rd());
        shuffle(selected.begin(), selected.end(), g);
        
        unordered_map<int, int> selected_cnt;
        for (int num : selected) {
            selected_cnt[num]++;
        }
        
        vector<int> remaining;
        for (int num : a) {
            if (selected_cnt.count(num) && selected_cnt[num] > 0) {
                selected_cnt[num]--;
            } else {
                remaining.push_back(num);
            }
        }
        
        unordered_map<int, int> cnt_selected;
        for (int num : selected) {
            cnt_selected[num]++;
        }
        vector<int> selected_counts;
        for (auto& [num, cnt] : cnt_selected) {
            selected_counts.push_back(cnt);
        }
        
        unordered_map<int, int> cnt_remaining;
        for (int num : remaining) {
            cnt_remaining[num]++;
        }
        vector<int> remaining_counts;
        for (auto& [num, cnt] : cnt_remaining) {
            remaining_counts.push_back(cnt);
        }
        
        i64 ans = count(selected_counts) * count(remaining_counts) % MOD;
        ans = ans * dp2[target] % MOD;
        
        cout << ans << '\n';
    }
    
    return 0;
}