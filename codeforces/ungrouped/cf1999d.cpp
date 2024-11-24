#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool solve(string s, string t, string &res) {
    int s_ptr = s.size() - 1;
    int t_ptr = t.size() - 1;
    res = "";

    while (t_ptr >= 0 && s_ptr >= 0) {
        if (s[s_ptr] == t[t_ptr] || s[s_ptr] == '?') {
            res += t[t_ptr];
            t_ptr--;
        } else {
            res += s[s_ptr];
        }
        s_ptr--;
    }

    // 如果t还有未匹配的字符，说明无法匹配
    if (t_ptr >= 0) {
        return false;
    }

    // 剩余的s如果有"?"，替换为"a"
    while (s_ptr >= 0) {
        res += (s[s_ptr] == '?' ? 'a' : s[s_ptr]);
        s_ptr--;
    }

    // 反转结果字符串
    reverse(res.begin(), res.end());
    return true;
}

int main() {
    int num_of_tc;
    cin >> num_of_tc;

    for (int i = 0; i < num_of_tc; ++i) {
        string s, t;
        cin >> s >> t;
        string res;
        if (solve(s, t, res)) {
            cout << "Yes" << endl;
            cout << res << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}
