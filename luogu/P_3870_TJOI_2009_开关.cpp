#include <functional>
#include <iostream>
#include <vector>
using namespace std;

class LazySegmentTree {
private:
    int n;
    int size;
    vector<int> tree;
    vector<bool> lazy;
    function<int(int, int)> merge;
    function<int(int, bool, int, int)> update;
    function<bool(bool, bool)> lazy_merge;
    int default_val;

    void build(const vector<int> &data) {
        for (int i = 0; i < n; ++i) {
            tree[size + i] = data[i];
        }
        for (int i = size - 1; i > 0; --i) {
            tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
        }
    }

    void push_down(int node, int node_left, int node_right) {
        if (lazy[node]) {
            int mid = (node_left + node_right) / 2;

            // Update left child
            int left_node = 2 * node;
            tree[left_node] =
                update(tree[left_node], lazy[node], node_left, mid);
            if (left_node < size) {  // Not a leaf
                lazy[left_node] = lazy_merge(lazy[left_node], lazy[node]);
            }

            // Update right child
            int right_node = 2 * node + 1;
            tree[right_node] =
                update(tree[right_node], lazy[node], mid + 1, node_right);
            if (right_node < size) {  // Not a leaf
                lazy[right_node] = lazy_merge(lazy[right_node], lazy[node]);
            }

            // Clear current node's lazy tag
            lazy[node] = false;
        }
    }

    int _range_query(int node, int node_left, int node_right, int query_l,
                     int query_r) {
        // No overlap
        if (query_r < node_left || node_right < query_l) {
            return 0;  // Default value for sum
        }

        // Complete overlap
        if (query_l <= node_left && node_right <= query_r) {
            return tree[node];
        }

        // Push down lazy tag
        push_down(node, node_left, node_right);

        int mid = (node_left + node_right) / 2;
        int left_val = _range_query(2 * node, node_left, mid, query_l, query_r);
        int right_val =
            _range_query(2 * node + 1, mid + 1, node_right, query_l, query_r);

        return merge(left_val, right_val);
    }

    void _range_update(int node, int node_left, int node_right, int update_l,
                       int update_r, bool tag) {
        // No overlap
        if (update_r < node_left || node_right < update_l) {
            return;
        }

        // Complete overlap
        if (update_l <= node_left && node_right <= update_r) {
            tree[node] = update(tree[node], tag, node_left, node_right);
            if (node < size) {  // Not a leaf
                lazy[node] = lazy_merge(lazy[node], tag);
            }
            return;
        }

        // Push down lazy tag
        push_down(node, node_left, node_right);

        int mid = (node_left + node_right) / 2;
        _range_update(2 * node, node_left, mid, update_l, update_r, tag);
        _range_update(2 * node + 1, mid + 1, node_right, update_l, update_r,
                      tag);

        // Update current node
        tree[node] = merge(tree[2 * node], tree[2 * node + 1]);
    }

public:
    LazySegmentTree(const vector<int> &data, function<int(int, int)> merge_func,
                    function<int(int, bool, int, int)> update_func,
                    function<bool(bool, bool)> lazy_merge_func,
                    int default_val = 0)
        : merge(merge_func), update(update_func), lazy_merge(lazy_merge_func),
          default_val(default_val) {
        n = data.size();
        size = 1;
        while (size < n) {
            size <<= 1;
        }

        tree.resize(2 * size, default_val);
        lazy.resize(2 * size, false);
        build(data);
    }

    int range_query(int l, int r) {
        return _range_query(1, 0, size - 1, l, r);
    }

    void range_update(int l, int r, bool tag) {
        _range_update(1, 0, size - 1, l, r, tag);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> data(n + 1, 0);

    auto merge_func = [](int a, int b) { return a + b; };
    auto update_func = [](int val, bool tag, int l, int r) {
        return tag ? (r - l + 1) - val : val;
    };
    auto lazy_merge_func = [](bool old_tag, bool new_tag) {
        return old_tag ^ new_tag;
    };

    LazySegmentTree seg_tree(data, merge_func, update_func, lazy_merge_func);

    while (m--) {
        int cmd;
        cin >> cmd;
        if (cmd == 0) {
            int l, r;
            cin >> l >> r;
            seg_tree.range_update(l, r, true);
        } else if (cmd == 1) {
            int l, r;
            cin >> l >> r;
            cout << seg_tree.range_query(l, r) << '\n';
        }
    }

    return 0;
}