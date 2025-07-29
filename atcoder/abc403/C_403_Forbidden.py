from collections import defaultdict

n, m, q = map(int, input().split())
mp = defaultdict(set)
for _ in range(q):
    cmd, data = input().split(maxsplit=1)
    match cmd:
        case "1":
            user, page = map(int, data.split())
            mp[user].add(page)
        case "2":
            user = int(data)
            mp[user].add(0)
        case "3":
            user, page = map(int, data.split())
            if 0 in mp[user] or page in mp[user]:
                print("Yes")
            else:
                print("No")
