#include <bits/stdc++.h>
#define forrange(i, start, end) \
    for (const auto i : std::ranges::iota_view{start, end})

signed main() {
    int n;
    std::cin >> n;
    forrange(i, 2, n + 1) {
        int sum = 0;
        forrange(j, 1, i) if (i % j == 0) sum += j;
        if (i == sum) std::cout << i << std::endl;
    }
    return 0;
}