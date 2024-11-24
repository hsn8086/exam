# print(int(str(eval(input()))[-4:]))
def mul(*args):
    res = None
    for i in args:
        if res is None:
            res = i
        else:
            res *= i
    return res if res else 0


inp = input()
spl_int = inp.split("+")
add_list = []
for i in spl_int:
    add_list.append(mul(*map(int, i.split("*"))))

print(sum(add_list) % 10000)
