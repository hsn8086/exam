import sys
import bisect

input = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, data, merge_func, update_func, lazy_merge_func, default_val=0):
        """
        初始化懒标记线段树

        参数:
        data: 原始数据数组
        merge_func: 合并两个值的函数 (lambda a, b: ...)
        update_func: 应用标记到值的函数 (lambda val, tag, l, r: ...)
        lazy_merge_func: 合并两个标记的函数 (lambda old_tag, new_tag: ...)
        default_val: 默认值，用于填充线段树末尾的空位
        """
        self.n = len(data)
        self.merge = merge_func
        self.update = update_func
        self.lazy_merge = lazy_merge_func
        self.default_val = default_val

        # 计算线段树的大小
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        # 初始化线段树和懒标记
        self.tree = [self.default_val] * (2 * self.size)
        self.lazy = [None] * (2 * self.size)

        # 构建线段树
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            left = self.tree[2 * i]
            right = self.tree[2 * i + 1]
            self.tree[i] = self.merge(left, right)

    def push_down(self, node, node_left, node_right):
        """
        将懒标记下推到子节点
        """
        if self.lazy[node] is not None:
            mid = (node_left + node_right) // 2

            # 更新左子节点
            left_node = 2 * node
            self.tree[left_node] = self.update(
                self.tree[left_node], self.lazy[node], node_left, mid
            )
            if left_node < self.size:  # 如果不是叶子节点
                self.lazy[left_node] = (
                    self.lazy_merge(self.lazy[left_node], self.lazy[node])
                    if self.lazy[left_node] is not None
                    else self.lazy[node]
                )

            # 更新右子节点
            right_node = 2 * node + 1
            self.tree[right_node] = self.update(
                self.tree[right_node], self.lazy[node], mid + 1, node_right
            )
            if right_node < self.size:  # 如果不是叶子节点
                self.lazy[right_node] = (
                    self.lazy_merge(self.lazy[right_node], self.lazy[node])
                    if self.lazy[right_node] is not None
                    else self.lazy[node]
                )

            # 清除当前节点的标记
            self.lazy[node] = None

    def range_query(self, l, r):
        """
        查询区间 [l, r] 的值
        """
        return self._range_query(1, 0, self.size - 1, l, r)

    def _range_query(self, node, node_left, node_right, query_l, query_r):
        """
        辅助函数：递归查询区间
        """
        # 当前节点区间与查询区间无交集
        if query_r < node_left or node_right < query_l:
            return None

        # 当前节点区间完全包含在查询区间内
        if query_l <= node_left and node_right <= query_r:
            return self.tree[node]

        # 需要下推懒标记
        self.push_down(node, node_left, node_right)

        mid = (node_left + node_right) // 2
        left_val = self._range_query(2 * node, node_left, mid, query_l, query_r)
        right_val = self._range_query(
            2 * node + 1, mid + 1, node_right, query_l, query_r
        )

        # 合并左右子树的结果
        if left_val is not None and right_val is not None:
            return self.merge(left_val, right_val)
        return left_val if left_val is not None else right_val

    def range_update(self, l, r, tag):
        """
        更新区间 [l, r] 的值，应用给定的标记
        """
        self._range_update(1, 0, self.size - 1, l, r, tag)

    def _range_update(self, node, node_left, node_right, update_l, update_r, tag):
        """
        辅助函数：递归更新区间
        """
        # 当前节点区间与更新区间无交集
        if update_r < node_left or node_right < update_l:
            return

        # 当前节点区间完全包含在更新区间内
        if update_l <= node_left and node_right <= update_r:
            self.tree[node] = self.update(self.tree[node], tag, node_left, node_right)
            if node < self.size:  # 如果不是叶子节点
                self.lazy[node] = (
                    self.lazy_merge(self.lazy[node], tag)
                    if self.lazy[node] is not None
                    else tag
                )
            return

        # 需要下推懒标记
        self.push_down(node, node_left, node_right)

        mid = (node_left + node_right) // 2
        self._range_update(2 * node, node_left, mid, update_l, update_r, tag)
        self._range_update(2 * node + 1, mid + 1, node_right, update_l, update_r, tag)

        # 更新当前节点的值
        left = self.tree[2 * node]
        right = self.tree[2 * node + 1]
        self.tree[node] = self.merge(left, right)


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = map(int, input().split())
    data = []
    init = [0] * (n + 1)
    for i, v in enumerate(a, 1):
        data.append([i, i, v])
        init[v] += 1

    seg_tree = LazySegmentTree(
        init,
        merge_func=lambda a, b: max(a, b),
        update_func=lambda val, tag, l, r: val + tag,
        lazy_merge_func=lambda old_tag, new_tag: (old_tag if old_tag is not None else 0)
        + new_tag,
    )

    for _ in range(m):
        print(data)
        l, r, d = map(int, input().split())
        idx_l = bisect.bisect(data, l, key=lambda x: x[1])
        idx_r = bisect.bisect(data, r, key=lambda x: x[0])
        pop_l, pop_r = False, False
        if data[idx_l][0] != data[idx_l][1]:
            seg_tree.range_update(l - data[idx_l][0] + d, d + data[idx_l][1] - l, -1)
            data[idx_l][1] = l - 1

        else:
            pop_l = True

        if data[idx_r][0] != data[idx_r][1]:
            seg_tree.range_update(d, r - data[idx_r][0] + d, -1)
            data[idx_r][1] = r + 1
        else:
            pop_r = True

        if pop_r:
            seg_tree.range_update(d, data[idx_r][1] - data[idx_r][0] + d, -1)
            data.pop(idx_r)

        for i in range(idx_r, idx_l):
            seg_tree.range_update(d, data[i][1] - data[i][0] + d, -1)
            data.pop(i)

        if pop_l:
            seg_tree.range_update(data[idx_l][1] - data[idx_l][0] + d, d, -1)
            data.pop(idx_l)

        # insort
        bisect.insort(data, [l, r, d], key=lambda x: x[0])

        seg_tree.range_update(d, data[idx_l][1] - data[idx_l][0] + d, 1)

        print(seg_tree.range_query(1, n))
