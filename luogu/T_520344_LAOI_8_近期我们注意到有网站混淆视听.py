from math import ceil

for _ in range(int(input())):
    s = input()
    if "LGR" not in s:
        print(0)
        continue
    print(min(ceil(s.count("CSP") / 2), ceil(s.count("LGR") / 2)))
