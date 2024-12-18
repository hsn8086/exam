
ntc = int(input())

for _ in range(ntc):
    m, a, b, c = map(int, input().split())

    row1 = min(m, a)
    row2 = min(m, b)

    rem1 = m - row1
    rem2 = m - row2

    if rem1 + rem2 >= c:
        total = row1 + row2 + c
    else:
        total = row1 + row2 + rem1 + rem2

    print(total)

