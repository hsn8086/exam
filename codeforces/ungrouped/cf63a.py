n = int(input())
lst = []
for i in range(n):
    name, type_ = input().split()
    lst.append((name, type_))
mapping = {"rat": 0, "woman": 1, "child": 1, "man": 2, "captain": 3}
lst.sort(key=lambda t: mapping[t[1]])
for i in lst:
    print(i[0])
