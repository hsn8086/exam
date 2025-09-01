#include <bits/stdc++.h>
using u64 = unsigned long long;
char buf[1 << 23], *p1 = buf, *p2 = buf;
#define gc()                                                                   \
    (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 21, stdin), p1 == p2)   \
         ? EOF                                                                 \
         : *p1++)
inline u64 rd() {// 读入一个 64 位无符号整数
    u64 x = 0;
    char ch = gc();
    while (!isdigit(ch)) ch = gc();
    while (isdigit(ch)) x = x * 10 + (ch ^ 48), ch = gc();
    return x;
}

int main() {
    u64 ans = 0;
    int n = rd();
    std::unordered_map<u64, u64> mp;
    u64 rnd = 23333;
    for (int i = 1; i <= n; ++i) {
        u64 x = rd(), y = rd();
        ans += i * mp[x + rnd];
        mp[x + rnd] = y;
    }
    std::cout << ans << std::endl;
    return 0;
}