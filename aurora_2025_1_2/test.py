import random


def data_gen(max_n, max_a,k_=False):
    if k_:
        n = max_n
        a = list(range(n))
        k = a[-1]
        return f'{n} {k}\n' + ' '.join(map(str, a))
    else:
        n = random.randint(1, max_n)
        a = [random.randint(1, max_a) for _ in range(n)]
        k = random.randint(1, sum(a))

        return f'{n} {k}\n' + ' '.join(map(str, a))


print(data_gen(10, 10))
