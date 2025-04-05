inp = int(input())
for i in range(1, 30):
    if i**i == inp:
        print(i)
        break
else:
    print(-1)
