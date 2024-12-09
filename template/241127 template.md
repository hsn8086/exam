# Binary Search
## Code
``` cpp
int binary_search(int start, int end, int key) {
  int ret = -1;  // 未搜索到数据返回-1下标
  int mid;
  while (start <= end) {
    mid = start + ((end - start) >> 1);  // 直接平均可能会溢出，所以用这个算法
    if (arr[mid] < key)
      start = mid + 1;
    else if (arr[mid] > key)
      end = mid - 1;
    else {  // 最后检测相等是因为多数搜索情况不是大于就是小于
      ret = mid;
      break;
    }
  }
  return ret;  // 单一出口
}
```
# Dijkstra
## Code
``` cpp

struct edge {
  int v, w;
};

struct node {
  int dis, u;

  bool operator>(const node& a) const { return dis > a.dis; }
};

vector<edge> e[MAXN];
int dis[MAXN], vis[MAXN];
priority_queue<node, vector<node>, greater<node>> q;

void dijkstra(int n, int s) {
  memset(dis, 0x3f, (n + 1) * sizeof(int));
  memset(vis, 0, (n + 1) * sizeof(int));
  dis[s] = 0;
  q.push({0, s});
  while (!q.empty()) {
    int u = q.top().u;
    q.pop();
    if (vis[u]) continue;
    vis[u] = 1;
    for (auto ed : e[u]) {
      int v = ed.v, w = ed.w;
      if (dis[v] > dis[u] + w) {
        dis[v] = dis[u] + w;
        q.push({dis[v], v});
      }
    }
  }
}

```

``` python
def dijkstra(graph, start):
    """
    Parameters:
    graph: adjacency list representation of the graph
    start: starting vertex

    Returns:
    distances: dictionary containing shortest distances from start to all vertices
    """
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)
        for neighbor, weight in graph[current]:
            if distances[neighbor] > distances[current] + weight:
                distances[neighbor] = distances[current] + weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))
    
    return distances
```
# Bubble Sort
## Code
``` python
def bubble_sort(a, n):
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if a[i] > a[i + 1]:
                flag = True
                a[i], a[i + 1] = a[i + 1], a[i]
```
``` cpp
void bubble_sort(int *a, int n) {
  bool flag = true;
  while (flag) {
    flag = false;
    for (int i = 1; i < n; ++i) {
      if (a[i] > a[i + 1]) {
        flag = true;
        int t = a[i];
        a[i] = a[i + 1];
        a[i + 1] = t;
      }
    }
  }
}
```
# KMP
## Code
``` python
def kmp(text, pattern):
    if not pattern:
        return 0

    # Build failure function
    failure = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            failure[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = failure[j-1]
        else:
            failure[i] = 0
            i += 1

    # Find pattern in text
    i = 0  # index in text
    j = 0  # index in pattern
    while i < len(text):
        if pattern[j] == text[i]:
            if j == len(pattern) - 1:
                return i - j
            i += 1
            j += 1
        elif j > 0:
            j = failure[j-1]
        else:
            i += 1
    return -1
```
# Merge Sort
## Code
``` python
def merge(a, b):
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        # <!> Check if b[j] < a[i] first to ensure stability
        if b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    # At this point, one array is empty and the other is not, merge the non-empty array into c
    c.extend(a[i:])
    c.extend(b[j:])
    return c

def merge_sort(a, ll, rr):
    if rr - ll <= 1:
        return
    # Divide
    mid = (rr + ll) // 2
    merge_sort(a, ll, mid)
    merge_sort(a, mid, rr)
    # Merge
    a[ll:rr] = merge(a[ll:mid], a[mid:rr])
```
``` cpp
void merge(const int *a, size_t aLen, const int *b, size_t bLen, int *c) {
  size_t i = 0, j = 0, k = 0;
  while (i < aLen && j < bLen) {
    if (b[j] < a[i]) {  // <!> First check if b[j] < a[i] to ensure stability
      c[k] = b[j];
      ++j;
    } else {
      c[k] = a[i];
      ++i;
    }
    ++k;
  }
// At this point, one array is empty, and the other array is not. Merge the non-empty array into c.
  for (; i < aLen; ++i, ++k) c[k] = a[i];
  for (; j < bLen; ++j, ++k) c[k] = b[j];
}

void merge_sort(int *a, int l, int r) {
    if (r - l <= 1) return;
    // Divide
    int mid = l + ((r - l) >> 1);
    merge_sort(a, l, mid);
    merge_sort(a, mid, r);
    // Merge
    int tmp[1024] = {};  // Adjust the length of the tmp array to match the length of a, or use a vector; first store the merged result in tmp, then copy back to array a
    merge(a + l, mid - l, a + mid, r - mid, tmp + l);  // pointer-style merge
    for (int i = l; i < r; ++i) a[i] = tmp[i];
}
```
# Newton's method
## isqrt
``` python
def isqrt_newton(n):
    x = 1
    decreased = False
    while True:
        nx = (x + n // x) // 2
        if x == nx or (nx > x and decreased):
            break
        decreased = nx < x
        x = nx
    ret
```
``` cpp
int isqrt_newton(int n) {
  int x = 1;
  bool decreased = false;
  for (;;) {
    int nx = (x + n / x) >> 1;
    if (x == nx || (nx > x && decreased)) break;
    decreased = nx < x;
    x = nx;
  }
  return x;
}
```
## fsqrt
``` python
def sqrt_newton(n):
    eps = 1e-15
    x = 1
    while True:
        nx = (x + n / x) / 2
        if abs(x - nx) < eps:
            break
        x = nx
    return x
```
``` cpp
double sqrt_newton(double n) {
  constexpr static double eps = 1E-15;
  double x = 1;
  while (true) {
    double nx = (x + n / x) / 2;
    if (abs(x - nx) < eps) break;
    x = nx;
  }
  return x;
}
```
## Normal
f(x) fd(x)
``` python
def newton_method(f, fd, x0, eps=1e-10, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < eps:
            return x
        x = x - fx / fd(x)
    return x
```
``` cpp
template<typename F1, typename F2>
double newton_method(F1 f, F2 fd, double x0, double eps = 1E-10, int max_iter = 100) {
    double x = x0;
    for (int i = 0; i < max_iter; i++) {
        double fx = f(x);
        if (abs(fx) < eps) return x;
        x = x - fx / fd(x);
    }
    return x;
}
```

# Optimization
## Python
### Recursion
``` python
import sys
sys.setrecursionlimit(10010)
```
### Sort
-  `functools.cmp_to_key(func)`

    将(旧式的)比较函数转换为新式的 key function . 在类似于 sorted() ， min() ， max() ， heapq.nlargest() ， heapq.nsmallest() ， itertools.groupby() 等函数的 key 参数中使用。此函数主要用作将 Python 2 程序转换至新版的转换工具，以保持对比较函数的兼容。

    比较函数意为一个可调用对象，该对象接受两个参数并比较它们，结果为小于则返回一个负数，相等则返回零，大于则返回一个正数。key function则是一个接受一个参数，并返回另一个用以排序的值的可调用对象。
### Cache
- `@functools.cache(user_function)`
  
    简单轻量级未绑定函数缓存。 有时称为 "memoize"。

    返回值与 lru_cache(maxsize=None) 相同，创建一个查找函数参数的字典的简单包装器。 因为它不需要移出旧值，所以比带有大小限制的 lru_cache() 更小更快。


- `@functools.lru_cache(maxsize=128, typed=False)`

    一个为函数提供缓存功能的装饰器，缓存 maxsize 组传入参数，在下次以相同参数调用时直接返回上一次的结果。用以节约高开销或I/O函数的调用时间。

    由于使用了字典存储缓存，所以该函数的固定参数和关键字参数必须是可哈希的。

    不同模式的参数可能被视为不同从而产生多个缓存项，例如, f(a=1, b=2) 和 f(b=2, a=1) 因其参数顺序不同，可能会被缓存两次。

# Counter
## 初始化方式

```python
c = Counter()                           # 空计数器
c = Counter('gallahad')                 # 从可迭代对象创建
c = Counter({'red': 4, 'blue': 2})      # 从字典创建  
c = Counter(cats=4, dogs=8)             # 从关键字参数创建
```

## 主要特性

- 访问不存在的键返回0而不是KeyError
- 设置计数为0不会删除元素，需使用del删除
- 继承dict的所有方法
- 3.7版本后保持插入顺序

## 特殊方法

1. `elements()`: 返回元素迭代器，每个元素重复其计数次
2. `most_common([n])`: 返回出现次数最多的n个元素
3. `subtract([iterable])`: 从另一个可迭代对象中减去元素计数
4. `update([iterable])`: 从另一个可迭代对象中增加元素计数

## 数学运算

支持以下运算符:

```python
c + d    # 相加: c[x] + d[x]
c - d    # 相减: 保持正计数
c & d    # 交集: min(c[x], d[x])
c | d    # 并集: max(c[x], d[x])
+c       # 保留正计数
-c       # 取反计数
```

## 常用操作

```python
sum(c.values())                 # 计数总和
c.clear()                       # 重置所有计数
list(c)                        # 唯一元素列表
dict(c)                        # 转换为普通字典
c.items()                      # 转换为(元素,计数)对列表
```
# Prefix sum
## 2-Dim prefix sum
### Build 2D prefix sum matrix
Given a 2-D matrix, we can calculate the prefix sum of the matrix. The prefix sum of matrix[i][j] is the sum of all elements in the rectangle whose top-left corner is (0, 0) and bottom-right corner is (i, j).
``` python
def build_prefix_sum(n: int, m: int) -> list:
    """Build 2D prefix sum matrix"""
    prefix_sum = []
    for i, row in enumerate(read_matrix_rows(n)):
        curr_row = []
        for j, val in enumerate(row):
            left = curr_row[-1] if curr_row else 0
            up = prefix_sum[i-1][j] if prefix_sum else 0
            diagonal = prefix_sum[i-1][j-1] if prefix_sum and j > 0 else 0
            curr_row.append(val + left + up - diagonal)
        prefix_sum.append(curr_row)
    return prefix_sum
```
```cpp
#include <vector>

std::vector<std::vector<int>> build_prefix_sum(int n, int m, const std::vector<std::vector<int>>& matrix) {
    std::vector<std::vector<int>> prefix_sum(n, std::vector<int>(m, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int left = (j > 0) ? prefix_sum[i][j-1] : 0;
            int up = (i > 0) ? prefix_sum[i-1][j] : 0;
            int diagonal = (i > 0 && j > 0) ? prefix_sum[i-1][j-1] : 0;
            prefix_sum[i][j] = matrix[i][j] + left + up - diagonal;
        }
    }
    return prefix_sum;
}
```
The time complexity of building the prefix sum matrix is O(nm), where n is the number of rows and m is the number of columns.

### Calculate the sum of a rectangle
2-D matrix prefix sum can be used to calculate the sum of a rectangle. But it is not as simple as 1-D prefix sum. We need to consider the overlapping area.
```python
def get_submatrix_sum(prefix_sum: list, x1: int, x2: int, y1: int, y2: int) -> int:
    """Calculate the sum of submatrix"""
    bottom = prefix_sum[x1-2][y2-1] if x1 > 1 and y2 > 0 else 0
    right = prefix_sum[x2-1][y1-2] if x2 > 0 and y1 > 1 else 0  
    overlap = prefix_sum[x1-2][y1-2] if x1 > 1 and y1 > 1 else 0
    return prefix_sum[x2-1][y2-1] - bottom - right + overlap
```
```cpp
int get_submatrix_sum(const std::vector<std::vector<int>>& prefix_sum, int x1, int x2, int y1, int y2) {
    int bottom = (x1 > 1 && y2 > 0) ? prefix_sum[x1-2][y2-1] : 0;
    int right = (x2 > 0 && y1 > 1) ? prefix_sum[x2-1][y1-2] : 0;
    int overlap = (x1 > 1 && y1 > 1) ? prefix_sum[x1-2][y1-2] : 0;
    return prefix_sum[x2-1][y2-1] - bottom - right + overlap;
}
```

