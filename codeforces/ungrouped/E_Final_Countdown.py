from itertools import accumulate

for _ in range(int(input())):
    length = int(input())
    prefix = list(accumulate(map(int, input())))
    lst = []
    carry = 0
    for now in prefix[::-1]:
        now += carry
        carry = now // 10
        lst.append(now % 10)
    lst.append(carry)
    print("".join(map(str, lst[::-1])).lstrip("0"))
