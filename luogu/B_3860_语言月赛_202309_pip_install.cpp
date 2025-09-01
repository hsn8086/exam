#include <bits/stdc++.h>
#define forrange(i, start, end) \
    for (const auto i : std::ranges::iota_view{start, end})

signed main() {
    // Fast io
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int n, k, tmp;
    std::cin >> n;
    std::vector<std::vector<int>> graph(n + 1);
    forrange(i, 1, n + 1) {
        std::cin >> k;
        forrange(_, 0, k) {
            std::cin >> tmp;
            graph.at(i).push_back(tmp);
        }
    }
    std::deque<int> deq;
    std::set<int> s;
    deq.push_back(1);
    while (deq.size()) {
        int now = deq.front();
        deq.pop_front();
        if (s.contains(now)) continue;
        s.insert(now);
        for (const auto v : graph[now]) deq.push_back(v);
    }
    std::cout << s.size();
    return 0;
}