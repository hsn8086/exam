n = input()
cnt = 0
for a, b in zip(input(), input()):
    if a != b:
        cnt += 1
print(cnt)