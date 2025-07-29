# def find(lst: list, idx: int):
#     if lst[idx] == idx:
#         return idx
#     lst[idx] = find(lst, lst[idx])
#     return lst[idx]


# def test(lst: list, a: int, b: int):
#     a_leader = find(lst, a)
#     b_leader = find(lst, b)
#     if a_leader == b_leader:
#         return True
#     return False


# def merge(lst: list, a: int, b: int):
#     a_leader = find(lst, a)
#     b_leader = find(lst, b)
#     if a_leader != b_leader:
#         lst[a_leader] = b_leader


# for _ in range(int(input())):
#     n, q = map(int, input().split())
#     hu = list(range(n + 1))
#     lst = list(range(n + 1))
#     mapp = list(range(n + 1))
#     rec = list(range(n + 1))
#     for _ in range(q):
#         cmdl = map(int, input().split())
#         cmd = next(cmdl)
#         if cmd == 1:
#             a, b = cmdl
#             merge(lst, b, a)
#         elif cmd == 2:
#             a, b = cmdl
#             hu[a] = rec[b]
#         elif cmd == 3:
#             a, b = cmdl
#             mapp[rec[a]], mapp[rec[b]] = mapp[rec[b]], mapp[rec[a]]
#             rec[a], rec[b] = rec[b], rec[a]

#         elif cmd == 4:
#             a = next(cmdl)
#             print(mapp,mapp[hu[a]])
#             print(mapp[find(lst, hu[a])])
#     print(rec, mapp)


class Clan:
    def __init__(self, id_):
        self.id_ = id_
        self.hu = set()
        self.chi=set()
        self.leader = self

    def find(self):
        if self.leader == self:
            return self
        node = self
        node = node.leader.find()
        self.leader = node
        return node

    def merge(self, b):
        a_leader = self.find()
        b_leader = b.find()
        if a_leader != b_leader:
            a_leader.leader = b



class Hu:
    def __init__(self, id_):
        self.id_ = id_
        self.clan: Clan | None = None

    def set(self, clan):
        self.clan = clan


for _ in range(int(input())):
    n, q = map(int, input().split())
    hu = [Hu(i) for i in range(n + 1)]
    clan = [Clan(i) for i in range(n + 1)]
    for h, c in zip(hu, clan):
        c.hu.add(h)
        h.clan = c
    for _ in range(q):
        cmdl = map(int, input().split())
        cmd = next(cmdl)
        if cmd == 1:
            a, b = cmdl
            clan[b].merge(clan[a])

        elif cmd == 2:
            a, b = cmdl
            hu[a].clan.hu.remove(hu[a])
            clan[b].hu.add(hu[a])
        elif cmd == 3:
            a, b = cmdl
            clan[a].hu, clan[b].hu = clan[b].hu, clan[a].hu
        elif cmd == 4:
            a = next(cmdl)
            print(hu[a].clan.leader.id_)
