n = int(input())

data = []
for i in range(n):
    inp = input().split()
    data.append((inp[0], *map(int, inp[1:]), n - i - 1))

data.sort(key=lambda a: a[1] * 1000000 + a[2] * 10000 + a[3] * 100 + a[4])
for i in data:
    print(i[0])
