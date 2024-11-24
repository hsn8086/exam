def count_unique_substrings(s, cache={}):
    if s in cache:
        return cache[s]

    substrings = set()
    n = len(s)
    for i in range(n):
        curr = ""
        for j in range(i, n):
            curr += s[j]
            substrings.add(curr)

    result = len(substrings)
    cache[s] = result
    return result


# t = int(input())
# for _ in range(t):
#     s = input().strip()
#     n = len(s)

#     found = False
#     # 从短到长检查,更容易找到答案
#     for start in range(n):
#         curr = ''
#         for j in range(start, n):
#             curr += s[j]
#             if count_unique_substrings(curr) % 2 == 0:
#                 print(curr)
#                 found = True
#                 break
#         if found:
#             break

#     if not found:
#         print(-1)

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    if n == 1:
        print(-1)
        continue

    found = False
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            print(s[i] + s[i + 1])
            found = True
            break
    if not found:
        for i in range(n - 2):
            if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i] != s[i + 2]:
                print(s[i] + s[i + 1] + s[i + 2])
                found = True
                break
    if not found:
        print(-1)
