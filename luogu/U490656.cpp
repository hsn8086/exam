#include <iostream>
#include <vector>
using namespace std;
int solve(const vector<vector<int>> square, int x1, int y1, int x2, int y2) {
    int sum = 0;
    for (int x = x1; x <= x2; ++x) {
        for (int y = y1; y <= y2; ++y) {
            sum += square[x - 1][y - 1];
        }
    }
    return sum;
}

int main() {
    int n, m, q;
    cin >> n >> m >> q;
    vector<vector<int>> square(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> square[i][j];
        }
    }
    for (int i = 0; i < q; ++i) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << solve(square, x1, y1, x2, y2) << endl;
    }
    return 0;
}