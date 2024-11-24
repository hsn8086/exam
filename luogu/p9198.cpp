#include <iostream>
#include <map>
#include <set>
#include <tuple>
using namespace std;

int main() {
    int n, m, q;
    cin >> n >> m >> q;

    map<tuple<int, int, int>, int> changed_map;  // To store changes
    set<tuple<int, int, int>> neq_set;  // To track unequal sets

    for (int query = 0; query < q; ++query) {
        int i, j, t, c;
        cin >> i >> j >> t >> c;

        // Update the map with the changes
        changed_map[make_tuple(i, j, t)] = (changed_map[make_tuple(i, j, t)] + c) % 256;

        // Check for inequality with the mirrored position
        if (changed_map[make_tuple(i, m - j + 1, t)] != changed_map[make_tuple(i, j, t)]) {
            cout << "No" << endl;
            neq_set.insert(make_tuple(i, j, t));
            continue;
        }

        // Manage the unequal set
        if (neq_set.count(make_tuple(i, j, t))) {
            neq_set.erase(make_tuple(i, j, t));
        }
        
        if (neq_set.count(make_tuple(i, m - j + 1, t))) {
            neq_set.erase(make_tuple(i, m - j + 1, t));
        }

        // Check the size of the unequal set
        if (neq_set.empty()) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}
