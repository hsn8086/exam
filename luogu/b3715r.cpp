#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <numeric>
#include <algorithm> // 引入算法库用于排序

using namespace std;

// Pollard's Rho algorithm for integer factorization
long long pollard_rho(long long n, int rt = 0) {
    if (n % 2 == 0) {
        return 2;  // 如果 n 是偶数，直接返回 2
    }

    // 定义轮转函数
    auto f = [n](long long x, long long c) {
        return (x * x + c) % n;
    };

    long long x = rand() % (n - 2) + 2;
    long long y = x;
    long long c = rand() % (n - 1) + 1;
    long long d = 1;

    while (d == 1) {
        x = f(x, c);
        y = f(f(y, c), c);
        d = __gcd(abs(x - y), n);
        if (d == n) {
            if (rt > 5) {
                return d;
            }
            return pollard_rho(n, rt + 1);  // 如果失败，重新尝试
        }
    }

    return d;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    srand(time(0));  // 用当前时间作为随机种子

    int ntc;
    cin >> ntc;  // 读取测试案例数量
    while (ntc--) {
        long long num;
        cin >> num;  // 读取待分解的数

        vector<long long> factors;
        while (num != 1) {
            long long f = pollard_rho(num);
            factors.push_back(f);
            num /= f;
        }

        // 对因子进行排序
        sort(factors.begin(), factors.end());

        // 输出排序后的因子
        for (size_t i = 0; i < factors.size(); ++i) {
            cout << factors[i];
            if (i < factors.size() - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
