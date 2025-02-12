input()
a = list(map(int, input()))
# a_sum = [0]
# for i in a:
#     a_sum.append(a_sum[-1] + i)

for _ in range(int(input())):
    left, right = map(int, input().split())
    zeros = [0]

    for i in a[left - 1 : right]:
        if i == 0:
            zeros[-1] += 1
        elif zeros[-1] != 0:
            zeros.append(0)
    s = sum(i * (i + 1) // 2 for i in zeros)
    k = right - left + 1
    print(k * (k + 1) // 2 - s)
