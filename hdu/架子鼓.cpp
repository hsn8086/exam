#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        unordered_set<int> s;
        int t = 0;
        for (int i = 0; i < n; ++i) {
            int p, q;
            cin >> p >> q;
            s.insert(t);
            t += p * (48 / q);
        }

        int cnt = 0;
        t = 0;
        for (int i = 0; i < m; ++i) {
            int p, q;
            cin >> p >> q;
            if (s.find(t) != s.end()) {
                cnt++;
            }
            t += p * (48 / q);
        }
        cout << cnt << endl;
    }
    return 0;
}