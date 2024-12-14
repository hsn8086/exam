from collections import Counter

ntc = int(input())
for _ in range(ntc):
    n = int(input())
    s = list(input())
    if len(s) == 1:
        print("".join(s))
        continue
    c = list(Counter(s).items())
    c.sort(key=lambda t:t[1])
    most=c[-1][0]
    least=c[0][0]
    s[s.index(least)]=most

    print("".join(s))
