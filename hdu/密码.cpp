#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int sol(int a, int b, int c) {
    if (a == 0) {
        return -1;
    }
    int numerator = c - b;
    if (numerator % a != 0) {
        return -1;
    }
    int x = numerator / a;
    return x >= 0 ? x : -1;
}

vector<int> generate_current_rsts(const vector<int>& triplet) {
    vector<int> current_rsts;
    int a, b, c;
    
    // Permutation 0,1,2
    a = triplet[0]; b = triplet[1]; c = triplet[2];
    int x = sol(a, b, c);
    if (x != -1) current_rsts.push_back(x);
    
    // Permutation 0,2,1
    a = triplet[0]; b = triplet[2]; c = triplet[1];
    x = sol(a, b, c);
    if (x != -1) current_rsts.push_back(x);
    
    // Permutation 1,0,2
    a = triplet[1]; b = triplet[0]; c = triplet[2];
    x = sol(a, b, c);
    if (x != -1) current_rsts.push_back(x);
    
    // Permutation 1,2,0
    a = triplet[1]; b = triplet[2]; c = triplet[0];
    x = sol(a, b, c);
    if (x != -1) current_rsts.push_back(x);
    
    // Permutation 2,0,1
    a = triplet[2]; b = triplet[0]; c = triplet[1];
    x = sol(a, b, c);
    if (x != -1) current_rsts.push_back(x);
    
    // Permutation 2,1,0
    a = triplet[2]; b = triplet[1]; c = triplet[0];
    x = sol(a, b, c);
    if (x != -1) current_rsts.push_back(x);
    
    return current_rsts;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    while (T--) {
        int K;
        cin >> K;
        vector<vector<int>> triplets(K);
        for (int i = 0; i < K; ++i) {
            int a, b, c;
            cin >> a >> b >> c;
            triplets[i] = {a, b, c};
        }
        vector<int> ans;
        bool found = false;
        for (int i = 0; i < K; ++i) {
            const auto& t = triplets[i];
            vector<int> current_rsts = generate_current_rsts(t);
            if (ans.empty()) {
                ans = current_rsts;
            } else {
                unordered_set<int> prev_set(ans.begin(), ans.end());
                vector<int> new_ans;
                for (int x : current_rsts) {
                    if (prev_set.count(x)) {
                        new_ans.push_back(x);
                    }
                }
                ans = new_ans;
            }
            if (ans.empty()) {
                break;
            }
            if (ans.size() == 1) {
                cout << ans[0] << '\n';
                found = true;
                break;
            }
        }
        if (!found && !ans.empty()) {
            cout << ans[0] << '\n';
        } else if (!found) {
            cout << -1 << '\n';
        }
    }
    return 0;
}