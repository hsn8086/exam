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
    ka, sa = a
    kb, sb = b
    if sa != sb:
        return sa < sb
    return ka > kb


n, m = map(int, input().split())
lst = []
for _ in range(n):
    k, s = map(int, input().split())
    lst.append((k, s))

merge_sort(lst,0,len(lst),cmp)
score=lst[m*3//2-1][1]
rst=[]

for k,s in lst:

    if s<score:
        break
    rst.append((k,s))

print(score,len(rst))

for k,s in rst:
    print(k,s)