#include <bits/stdc++.h>

int fib(int a) {
    if (a <= 2) return 1;
    return fib(a - 1) + fib(a - 2);
}

signed main() {
    int n, a;
    std::cin >> n;
    while (n--) {
        std::cin >> a;
        std::cout << fib(a) << std::endl;
    }
    return 0;
}