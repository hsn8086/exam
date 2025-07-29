import sys


def search(id_, a, cnt, tag, start):
    stop = start
    tag[start] = id_
    start = a[start]
    cnt_ = 1
    while stop != start:
        tag[start] = id_
        start = a[start]
        cnt_ += 1
    cnt[id_] += cnt_


input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx])
idx += 1
for _ in range(t):
    n = int(data[idx])
    idx += 1
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[idx])
        idx += 1
    cnt = [0] * 100010
    tag = [0] * 100010
    d = list(map(int, data[idx : idx + n]))
    idx += n

    id_ = 0
    for i in range(1, n + 1):
        if not tag[i]:
            id_ += 1
            search(id_, a, cnt, tag, i)

    cnt_ = 0
    output = []
    for i in range(n):
        current_tag = tag[d[i]]
        if cnt[current_tag]:
            cnt_ += cnt[current_tag]
            cnt[current_tag] = 0
        output.append(str(cnt_))
    print(" ".join(output))
