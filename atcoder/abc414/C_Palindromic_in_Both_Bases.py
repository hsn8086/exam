from itertools import product

a = int(input())
n = int(input())


def trans(n: int, base: int) -> list:
    ans = []
    while n > 0:
        ans.append(n % base)
        n //= base
    return ans[::-1]


def check(n: int, base: int) -> bool:
    digits = trans(n, base)
    return digits == digits[::-1]


ans = 0


for length in range(1, 13):
    half = (length + 1) // 2
    for lst in product(range(10), repeat=half):
        if lst[0] == 0:
            continue

        if length % 2 == 0:
            pal = lst + lst[::-1]
        else:
            pal = lst + lst[:-1][::-1]
        num = int("".join(map(str, pal)))
        if num > n:
            if length % 2 == 0:
                break
            continue
        if check(num, a):
            ans += num

print(ans)
