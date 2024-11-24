def search(a, m, n):
    q = set()

    q.add(n)

    max_l = 0
    try:
        while 1:
            n = q.pop()
            max_l = max(n, max_l)
            for i in m.get(n, []):
                if i:
                    q.add(n + i)
    except KeyError:
        return max_l


def solve(n, a):
    # m={a[i]+i+1:i for i in range(len(a))}
    m = {}
    for i in range(n):
        if a[i] + i not in m:
            m[a[i] + i] = []
        m[a[i] + i].append(i)
    return search(a, m, n)


num_of_tc = int(input())
for i in range(num_of_tc):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
# import random

# print(solve(10**5, [random.randint(1, 10**9) for i in range(10**5)]))
