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
