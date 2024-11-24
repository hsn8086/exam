#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> queries(m);
    for (int i = 0; i < m; ++i) {
        cin >> queries[i];
    }

    vector<int> results(m);
    for (int i = 0; i < m; ++i) {

        auto it = lower_bound(a.begin(), a.end(), queries[i]);

        if (it != a.end() && *it == queries[i]) {
            results[i] = it - a.begin() + 1;
        } else {
            results[i] = -1;
        }
    }

    for (int i = 0; i < m; ++i) {
        cout << results[i];
        if (i < m - 1) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}
