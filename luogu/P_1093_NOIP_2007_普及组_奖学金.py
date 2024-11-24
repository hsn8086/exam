def merge(a, b, cmp_f):
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if cmp_f(a[i], b[j]):
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c


def merge_sort(a, ll, rr, cmp_f):
    if rr - ll <= 1:
        return a[ll:rr]
    mid = (ll + rr) // 2
    merge_sort(a, ll, mid, cmp_f)
    merge_sort(a, mid, rr, cmp_f)
    a[ll:rr] = merge(a[ll:mid], a[mid:rr], cmp_f)


def cmp(a, b):
    ca, ma, ea, ia = a
    cb, mb, eb, ib = b
    tola = ca + ma + ea
    tolb = cb + mb + eb

    if tola != tolb:
        return tolb > tola 
    if ca != cb:
        return cb > ca
    return ib < ia


lst = []
n = int(input())
for i in range(n):
    c, m, e = map(int, input().split())
    lst.append((c, m, e, i + 1))
merge_sort(lst, 0, len(lst), cmp)
for c, m, e, i in lst[:5]:
    print(i, c + m + e)
