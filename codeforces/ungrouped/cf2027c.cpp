#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <unordered_set>
using namespace std;

long long search(const vector<long long>& a, unordered_map<long long, vector<long long>>& m, long long n) {
    queue<long long> q;
    unordered_set<long long> visited;  // 记录已访问节点
    q.push(n);
    visited.insert(n);

    long long max_l = 0;
    while (!q.empty()) {
        long long current = q.front();
        q.pop();
        max_l = max(current, max_l);
        for (long long i : m[current]) {
            long long next = current + i;
            if (visited.find(next) == visited.end()) {  // 如果未访问过
                q.push(next);
                visited.insert(next);  // 标记为已访问
            }
        }
    }
    return max_l;
}

long long solve(long long n, const vector<long long>& a) {
    unordered_map<long long, vector<long long>> m;
    for (long long i = 0; i < n; ++i) {
        m[a[i] + i].push_back(i);
    }
    return search(a, m, n);
}

int main() {
    int num_of_tc;
    cin >> num_of_tc;
    while (num_of_tc--) {
        long long n;
        cin >> n;
        vector<long long> a(n);
        for (long long i = 0; i < n; ++i) {
            cin >> a[i];
        }
        cout << solve(n, a) << endl;
    }
    return 0;
}
