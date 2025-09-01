#include <bits/stdc++.h>

using i64 = int64_t;

class FenwickTree {
private:
    int size;
    std::vector<i64> tree;

public:
    explicit FenwickTree(int n) : size(n), tree(n + 1, 0) {}

    void update(int index, i64 delta) {
        while (index <= size) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    i64 query_prefix(int index) const {
        i64 res = 0;
        while (index > 0) {
            res += tree[index];
            index -= index & -index;
        }
        return res;
    }

    i64 query(int index) const {
        return query_range(index, index);
    }

    i64 query_range(int left, int right) const {
        return query_prefix(right) - query_prefix(left - 1);
    }
};


class RURQFenwickTree {
private:
    FenwickTree ft1, ft2;

    void _update(int index, i64 delta) {
        ft1.update(index, delta);
        ft2.update(index, delta * index);
    }

public:
    explicit RURQFenwickTree(int n) : ft1(n), ft2(n) {}

    void update(int index, i64 delta) {
        update_range(index, index, delta);
    }

    void update_range(int left, int right, i64 delta) {
        _update(left, delta);
        _update(right + 1, -delta);
    }

    i64 query_prefix(int index) const {
        return (index + 1) * ft1.query_prefix(index) - ft2.query_prefix(index);
    }

    i64 query(int index) const {
        return query_range(index, index);
    }

    i64 query_range(int left, int right) const {
        return query_prefix(right) - query_prefix(left - 1);
    }
};


int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    std::cin >> n >> m;
    std::vector<i64> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        std::cin >> a[i];
    }

    RURQFenwickTree rurq_ft(n);
    for (int i = 1; i <= n; ++i) {
        rurq_ft.update(i, a[i]);
    }

    for (int i = 0; i < m; ++i) {
        int cmd;
        std::cin >> cmd;
        if (cmd == 1) {
            int x, y;
            i64 k;
            std::cin >> x >> y >> k;
            rurq_ft.update_range(x, y, k);
        } else if (cmd == 2) {
            int x, y;
            std::cin >> x >> y;
            std::cout << rurq_ft.query_range(x, y) << "\n";
        }
    }

    return 0;
}
