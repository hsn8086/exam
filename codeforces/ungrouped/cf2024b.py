def solve(n, k, a):
    a = list(a)
    a.sort(reverse=True)
    count = 0
    height = 0
    while k > 0:
        if k > (a[-1] - height) * len(a):
            k -= (a[-1] - height) * len(a)
            count += (a[-1] - height) * len(a)
            height = a[-1]
            while a[-1] == height:
                count += 1
                a.pop(-1)

        else:
            count += k
            k = 0
    return count


num_of_tc = int(input())
for _ in range(num_of_tc):
    n, k = map(int, input().split())
    a = map(int, input().split())
    print(solve(n, k, a))
