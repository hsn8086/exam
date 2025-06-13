n = map(int, input().split())
s = set(input())

for v in s:
    if v.upper() not in s or v.lower() not in s:
        print("NO")
        break
else:
    print("YES")

#
