from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(input())
    # print("a",*a)
    cnt = Counter(a)
    if cnt["0"] != cnt["1"]:
        print(-1)
        continue
    length = n
    cur = 0
    ins = []
    while a:
        if a[0] != a[-1]:
            cur += 1
            a.pop(-1)
            a.pop(0)
        elif a[0] == a[-1] == "0":
            ins.append(length - cur)
            length += 2
            a = a + ["0", "1"]
        elif a[0] == a[-1] == "1":
            ins.append(cur)

            length += 2
            a = ["0", "1"] + a
    print(len(ins))
    print(*ins)
"0 1 1 0 0 1 0 1"