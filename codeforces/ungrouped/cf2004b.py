def solve(al: int, ar: int, bl: int, br: int):
    ml, mr = max(al, bl), min(ar, br)
    rt = mr - ml
    if not (ml == al and ml == bl):
        rt += 1
    if not (mr == ar and mr == br):
        rt += 1
    if rt <= 0:
        rt = 1
    return rt


cotc = int(input())
for i in range(cotc):
    al, ar = map(int, input().split())
    bl, br = map(int, input().split())
    print(solve(al, ar, bl, br))
