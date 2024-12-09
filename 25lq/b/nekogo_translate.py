inp = input()

for i in inp:
    if ord(i) < 128:
        print(i, end="")
    else:
        print("喵", end="")
print()
