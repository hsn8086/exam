from dataclasses import dataclass

@dataclass
class Item:
    value: int
    index: int
def cmp(a, b):
    if a.value < b.value:
        return True
    elif a.value == b.value and a.index > b.index:
        return True

    return False
def merge(a, b):
    i, j = 0, 0
    c = []
    inv_count = 0
    while i < len(a) and j < len(b):
        if not cmp(a[i], b[j]):
            c.append(b[j])
            inv_count += len(a) - i
            j += 1
        else:
            c.append(a[i])
            i += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c, inv_count

def merge_sort(a, ll, rr):
    if rr - ll <= 1:
        return 0
    mid = (rr + ll) // 2
    inv_count = merge_sort(a, ll, mid)
    inv_count += merge_sort(a, mid, rr)
    result, count = merge(a[ll:mid], a[mid:rr])
    a[ll:rr] = result
    return inv_count + count

ntc = int(input())
for _ in range(ntc):
    n = int(input())
    arr = list(map(int, input().split()))
    items = [Item(value=x, index=i) for i, x in enumerate(arr)]
    result = merge_sort(items, 0, n)
    print(result)
