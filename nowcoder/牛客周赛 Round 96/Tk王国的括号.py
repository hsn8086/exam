import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
s = list(map(ord, input()))


def del_lst(lst, l, r):
    # print(lst)
    if (l - 1 >= 0 and r + 1 < len(lst)) and (
        lst[l - 1] + lst[r + 1] == 219 or lst[l - 1] + lst[r + 1] == 155
    ):
        return 1 + del_lst(lst, l - 1, r + 1)
    del lst[l : r + 1]
    return 1


i = -1
diff = 0
while True:
    i += 1
    i -= diff
    if i >= len(s) - 1:
        break
    diff = 0

    if s[i] + s[i + 1] == 219 or s[i] + s[i + 1] == 155:
        diff = del_lst(s, i, i + 1)

print(len(s))
