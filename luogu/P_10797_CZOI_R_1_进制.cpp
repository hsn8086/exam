#include <iostream>
#include <cmath>
using namespace std;

const long long MOD = 1e9 + 7;

pair<long long, long long> calc_first_num(long long num, long long x) {
    if (num == 0) return {0, 1};
    long long count = 0;
    long long tmp = num;
    while (tmp) {
        tmp /= x;
        count++;
    }
    return {num / (long long)pow(x, count - 1), count};
}

long long add(long long num) {
    long long x = 2;
    while (true) {
        auto [first, count] = calc_first_num(num, x);
        if (first <= x - 2) {
            return num + (long long)pow(x, count - 1) % MOD;
        }
        x++;
        if (x > first + 2) {
            return num + 1;
        }
    }
}

int main() {
    int ntc;
    cin >> ntc;
    while (ntc--) {
        long long num, n;
        cin >> num >> n;
        while (n--) {
            num = add(num) % MOD;
        }
        cout << num << endl;
    }
    return 0;
}
