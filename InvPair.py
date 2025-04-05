def merge_sort(s,l,r):
    if l >= r: return 0
    mid = l + r >> 1
    res = merge_sort(s,l,mid) + merge_sort(s,mid + 1,r)
    i = l
    j = mid + 1
    tmp = []
    while(i <= mid and j <= r):
        if(s[i] <= s[j]):
            tmp.append(s[i])
            i += 1
        else:
            res += (mid - i + 1)
            tmp.append(s[j])
            j += 1
            pass
        pass
    while(i <= mid):
        tmp.append(s[i])
        i += 1
        pass
    while(j <= r):
        tmp.append(s[j])
        j += 1
        pass
    s[l:r + 1] = tmp
    return res


n = eval(input())
s = list(map(int,input().split()))
print(merge_sort(s, 0, n - 1))
