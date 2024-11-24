#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
int main() {
    int n, m, r;
    cin >> n >> m >> r;
    vector<tuple<int, int>> lst;
    int i;
    while (m--) {
        int a, b;
        cin >> a >> b;
        lst.push_back(make_tuple(a, b));
    }
    int count = 0;
    for (int x = 1; x <= n; x++) {
        for (int y = 1; y <= n; y++) {
            for (auto t : lst) {
                auto [xm, ym] = t;
                if ((x - xm) * (x - xm) + (y - ym) * (y - ym) <= r * r) {
                    count++;
                    break;
                }
            }
        }
    }
    cout << count;
    return 0;
}