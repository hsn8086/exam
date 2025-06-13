#include <bits/stdc++.h>
using namespace std;
const int eps = 1e-9;
int main() {
    int n;
    cin >> n;
    for (int i = 1; i < n / 2 + 1; i++)
        if (1 + 4 * ((double)n * 2 + i * i - i) >= 0) {
            double t = (sqrt(1 + 4 * ((double)n * 2 + i * i - i)) - 1) / 2;
            int t1 = (int)t;
            if (t == t1 && t1 > i) printf("%d %d\n", i, t1);
        }
    return 0;
}