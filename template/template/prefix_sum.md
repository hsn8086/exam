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