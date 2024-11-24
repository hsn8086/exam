#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    std::ios::sync_with_stdio(0);
    const int MAX = 100000000;
    vector<bool> lst(MAX + 1, true);
    lst[0] = lst[1] = false; // 0 和 1 不是素数

    for (int i = 2; i <= sqrt(MAX); ++i) {
        if (!lst[i]) {
            continue;
        }
        for (long long j = i; i * j <= MAX; ++j) {
            lst[i * j] = false;
        }
    }

    vector<int> primes;
    for (int i = 0; i <= MAX; ++i) {
        if (lst[i]) {
            primes.push_back(i);
        }
    }

    int n, ntc;
    cin >> n >> ntc;
    for (int i = 0; i < ntc; ++i) {
        int inp;
        cin >> inp;
        cout << primes[inp - 1] << endl; // 素数的索引是从 0 开始的
    }

    return 0;
}
