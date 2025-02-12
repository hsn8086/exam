from itertools import chain

for _ in range(int(input())):
    n, m = map(int, input().split())
    lsts = []
    for _ in range(n):
        lsts.append(list(map(int, input().split())))
    lsts.sort(key=lambda lst: sum(lst), reverse=True)
    score = 0
    all_len = sum(map(len, lsts))
    for i, num in enumerate(chain.from_iterable(lsts)):
        score += num * (all_len - i)
    print(score)
