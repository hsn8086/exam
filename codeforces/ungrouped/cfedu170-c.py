def solve(n, k, a):
    a = list(a)
    a.sort()
    length = max(a)
    count_list = [0 for i in range(length + 1)]

    for i in a:
        count_list[i] += 1

    count_list_list = [[]]
    for i in count_list:
        if i == 0:
            if count_list_list[-1]:
                count_list_list.append([])
        else:
            count_list_list[-1].append(i)
    count_list_list = list(filter(lambda a: len(a), count_list_list))
    c_list = []
    for lst in count_list_list:
        current = sum(lst[:k])
        c_list.append(current)
        for i in range(k, len(lst)):
            current += lst[i] - lst[i - k]
            c_list.append(current)

    return max(c_list)


num_of_tc = int(input())
for _ in range(num_of_tc):
    n, k = map(int, input().split())
    a = map(int, input().split())
    print(solve(n, k, a))
