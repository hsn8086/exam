num_of_tc = int(input())

for _ in range(num_of_tc):
    count = 0
    a = input()
    b = input()
    if len(b) > len(a):
        a, b = b, a
    for i, v in enumerate(a):
        if i > len(b) - 1 or v != b[i]:
            break
        count += 1
    if count != 0:
        print(len(b) + len(a) - count + 1)
    else:
        print(len(b) + len(a))
