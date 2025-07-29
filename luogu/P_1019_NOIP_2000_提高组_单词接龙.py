from collections import defaultdict


def dfs(lst: list, start: str, visited: dict):
    if visited[start] == 2:
        return 0
    visited = visited.copy()
    visited[start] += 1
    ans = len(start)
    for i in lst:
        for j in range(1, len(start)):
            if i.startswith(start[-j:]):
                ans = max(ans, len(start) + dfs(lst, i, visited) - j)
                break

    return ans


lst = []
for _ in range(int(input())):
    lst.append(input())

print(dfs(lst, "1" + input(), defaultdict(int)) - 1)
