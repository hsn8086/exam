#include <bits/stdc++.h>
#include <iostream>
using i64 = long long;
inline void read(int &X) {
    X = 0;
    int w = 0;
    char ch = 0;
    while (!isdigit(ch)) w |= ch == '-', ch = getchar();
    while (isdigit(ch)) X = (X << 3) + (X << 1) + (ch ^ 48), ch = getchar();
    X = w ? -X : X;
}

int main() {
    int n;
    read(n);
    i64 ans = 0;
    for (int i = 1; i <= n; ++i) {
        int x;
        read(x);
        ans += x;
    }
    std::cout << ans << std::endl;
}