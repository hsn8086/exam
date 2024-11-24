#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(int n, int k, vector<int>& a) {
    sort(a.begin(), a.end());
    int count = 0;
    int height = 0;

    while (k > 0) {
        if (k > (a[0] - height) * a.size()) {
            k -= (a[0] - height) * a.size();
            count += (a[0] - height) * a.size();
            height = a[0];

            while (!a.empty() && a[0] == height) {
                count++;
                a.erase(a.begin());
            }
        } else {
            count += k;
            k = 0;
        }
    }
    
    return count;
}

int main() {
    int num_of_tc;
    cin >> num_of_tc;

    for (int i = 0; i < num_of_tc; ++i) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);

        for (int j = 0; j < n; ++j) {
            cin >> a[j];
        }

        cout << solve(n, k, a) << endl;
    }

    return 0;
}
