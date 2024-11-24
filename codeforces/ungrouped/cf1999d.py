# def solve(s, t):
#     res = ""
#     idx = 0
#     for i in t:
#         while idx < len(s) and s[idx] != i and s[idx] != "?":
#             res += s[idx]
#             idx += 1
#         if idx >= len(s):
#             yield "No"
#             return
#         if s[idx] == "?":
#             res += i
#             idx += 1
#     while idx < len(s):
#         res += s[idx] if s[idx] != "?" else "a"
#         idx += 1

#     yield "Yes"
#     # for i in range(len(s)):
#     #     if s[i] == "?":
#     #         s[i] = "a"

#     yield res


def solve(s, t):
    s_ptr = len(s) - 1
    t_ptr = len(t) - 1
    res = ""
    while t_ptr >= 0 and s_ptr >= 0:
        if s[s_ptr] == t[t_ptr] or s[s_ptr] == "?":
            res += t[t_ptr]
            t_ptr -= 1
        else:
            res += s[s_ptr]
        s_ptr -= 1
    if t_ptr >= 0:
        yield "No"
        return
    while s_ptr >= 0:
        res += s[s_ptr] if s[s_ptr] != "?" else "a"
        s_ptr -= 1
    yield "Yes"
    yield res[::-1]


num_of_tc = int(input())
for _ in range(num_of_tc):
    s = input()
    t = input()
    for i in solve(s, t):
        print(i)
