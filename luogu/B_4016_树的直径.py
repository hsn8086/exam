# from array import array
# import sys


# def event_loop(s):
#     stk, last_rst = [s], None
#     while stk:
#         try:
#             func, last_rst = stk[-1].send(last_rst), None
#             stk.append(func)
#         except StopIteration as e:
#             last_rst = e.value
#             stk.pop()
#     return last_rst


# def num_reader():
#     cache = 0
#     flag = False
#     while d := sys.stdin.buffer.read(1 << 8):
#         for i in d:
#             if i < 48 or i > 57:
#                 if flag:
#                     yield cache
#                     del cache
#                 cache = 0
#                 flag = False

#             else:
#                 flag = True
#                 cache *= 10
#                 cache += i - 48
#     if flag:
#         yield cache


# def dfs(e: dict[int, list], start: int, level: int, visited: bytearray, id_=1):
#     if visited[start] == id_:
#         return (start, level)
#     visited[start] = id_

#     max_ = (start, level)
#     for v in e[start]:
#         vex, lev = yield dfs(e, v, level + 1, visited, id_)
#         max_ = max(max_, (vex, lev), key=lambda t: t[1])

#     return max_


# inp = num_reader()
# n = next(inp)
# e = [array("I") for _ in range(n + 1)]
# for _ in range(n - 1):
#     u, v = next(inp), next(inp)
#     e[u].append(v)
#     e[v].append(u)

# ba = bytearray(n + 2)
# vex, _ = event_loop(dfs(e, 1, 0, ba, 1))
# _, lev = event_loop(dfs(e, vex, 0, ba, 2))
# print(lev)


