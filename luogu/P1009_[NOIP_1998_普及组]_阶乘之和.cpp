#include <bits/stdc++.h>
#define forrange(i, start, end) for (int i = start; i < end; i++)

std::vector<int> carry(std::vector<int> a) {
    forrange(i, 0, a.size() - 1) {
        auto div = a[i] / 10, mod = a[i] % 10;
        a[i + 1] += div;
        a[i] = mod;
    }
    while (!a.back()) a.pop_back();
    return a;
}
std::vector<int> mul(std::vector<int> a, std::vector<int> b) {
    auto length = std::max(a.size(), b.size());
}

int main() {}