#include <bits/stdc++.h>

#include <cstdio>
#define endl '\n'
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;
using f128 = long double;
constexpr long double pi =
    3.141592653589793238462643383279502884197169399375105L;

void solve() {
    int n, px, py;
    std::cin >> n >> px >> py;
    std::vector<std::tuple<int, int, int>> pts_max, pts_min;
    i64 max_d = 0, min_d = 1LL << 60;
    for (int i = 0; i < n; ++i) {
        int x, y;
        std::cin >> x >> y;
        i64 d = (i64)(x - px) * (x - px) + (i64)(y - py) * (y - py);
        if (d > max_d) {
            max_d = d;
            pts_max.clear();
            pts_max.emplace_back(x - px, y - py, i);
        } else if (d == max_d) {
            pts_max.emplace_back(x - px, y - py, i);
        }
        if (d < min_d) {
            min_d = d;
            pts_min.clear();
            pts_min.emplace_back(x - px, y - py, i);
        } else if (d == min_d) {
            pts_min.emplace_back(x - px, y - py, i);
        }
    }
    std::vector<f128> degrees_far, degrees_near;
    for (auto &[x, y, idx] : pts_max) degrees_far.push_back(atan2l(x, y));
    std::sort(degrees_far.begin(), degrees_far.end());
    for (auto deg : degrees_far) degrees_far.push_back(deg + 2 * pi);

    bool flag = false;
    std::vector<int> idx_lst;
    for (auto &[x, y, idx] : pts_min) idx_lst.push_back(idx);
    std::sort(idx_lst.begin(), idx_lst.end());
    for (size_t i = 1; i < idx_lst.size(); ++i) {
        if (idx_lst[i] - idx_lst[i - 1] == 1) {
            flag = true;
            break;
        }
    }
    if (!flag) {
        for (auto &[x, y, idx] : pts_min) degrees_near.push_back(atan2l(x, y));
        std::sort(degrees_near.begin(), degrees_near.end());
        for (auto deg : degrees_near) degrees_near.push_back(deg + 2 * pi);
    }

    if (flag) {
        printf("%.32Lf\n", 2 * pi);
    } else {
        f128 ans = 0;
        for (size_t i = 0; i + 1 < degrees_far.size(); ++i)
            ans = std::max(ans, degrees_far[i + 1] - degrees_far[i]);
        for (size_t i = 0; i + 1 < degrees_near.size(); ++i)
            ans = std::max(ans, degrees_near[i + 1] - degrees_near[i]);
        printf("%.32Lf\n", ans);
    }
}
signed main() {
    int t = 1;
    std::cin >> t;
    while (t--) solve();
    return 0;
}