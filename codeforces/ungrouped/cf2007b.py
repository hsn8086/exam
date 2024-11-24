from typing import Iterable


def solve(m: int, n: int, max_num: int, rules: Iterable[str]) -> list[int]:
    for rule in rules:
        if not rule:
            continue
        op, left, right = rule.split()
        lint, rint = int(left), int(right)
        if lint <= max_num <= rint:
            if op == "+":
                max_num += 1
            else:
                max_num -= 1
        yield max_num
    return


count_of_tc = int(input())
for i in range(count_of_tc):
    n, m = map(int, input().split())
    max_int = max(map(int, input().split()))
    rules = (input() for _ in range(m))
    rt = solve(m, n, max_int, rules)
    print(*rt)
"""
1
5 5
1 2 3 2 1
+ 1 3
- 2 3
+ 1 2
+ 2 4
- 6 8
5 5
1 3 3 4 5
+ 1 4
+ 2 3
- 4 5
- 3 3
- 2 6
5 5
1 1 1 1 1
+ 2 3
- 4 5
+ 1 6
- 2 5
+ 1 8
1 1
1
- 1 1
1 1
1000000000
+ 1000000000 1000000000
"""
