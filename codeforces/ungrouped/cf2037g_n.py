def pre(n):
    pri = []
    not_prime = [False] * (n + 1)
    for i in range(2, n + 1):
        if not not_prime[i]:
            pri.append(i)
        for pri_j in pri:
            if i * pri_j > n:
                break
            not_prime[i * pri_j] = True
            if i % pri_j == 0:
                break
    return pri


def break_down(n, pri):
    for pri_j in pri:
        if n % pri_j == 0:
            yield pri_j
            while n % pri_j == 0:
                n //= pri_j
    if n > 1:
        yield n

def check(ai, bi, bd_lst):
    for i in bd_lst[ai]:
        if i in bd_lst[bi]:
            return True
    return False


pri = pre(1000)
n = int(input())
a = list(map(int, input().split()))
bd_lst = [0] * n
for i in range(n):
    bd_lst[i] = list(break_down(a[i], pri))

lst = [1] * n
for i in range(1, n):
    sum_ = 0
    for j in range(0, i):
        if check(i, j, bd_lst):
            sum_ += lst[j]
    lst[i] = sum_

print(lst[-1])