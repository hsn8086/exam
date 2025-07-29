s = input()
lst = ["lqb", "lbq", "qlb", "qbl", "blq", "bql"]

cnt = 0
for i in lst:
    if i in s:
        cnt += 1

print(cnt)
