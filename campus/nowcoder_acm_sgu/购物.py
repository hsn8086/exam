n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
vlst = []
for i in range(m):
    vlst.append([int(input()), i, 0])
vlst.sort(key=lambda t: t[0])
val = 0
ptr = 0
for i, v in enumerate(a):
    val += v
    while ptr < len(vlst) and vlst[ptr][0] < val:
        vlst[ptr][2] = max(0, i)
        ptr += 1
while ptr < len(vlst):
        vlst[ptr][2] = max(0, i+1)
        ptr += 1
vlst.sort(key=lambda t: t[1])
for _, _, i in vlst:
    print(i)
