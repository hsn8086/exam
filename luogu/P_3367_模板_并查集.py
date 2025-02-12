# class Disjoin:
#     def __init__(self, id_):
#         self.id = id_
#         self.leader = self

#     def find(self):
#         if self.leader == self:
#             return self
#         node = self
#         node = node.leader.find()
#         self.leader = node
#         return node

#     def test(self, b: "Disjoin"):
#         a_leader = self.find()
#         b_leader = b.find()
#         if a_leader == b_leader:
#             return True
#         return False

#     def merge(self, b: "Disjoin"):
#         a_leader = self.find()
#         b_leader = b.find()
#         if a_leader != b_leader:
#             a_leader.leader = b

# def __repr__(self):
#     return f"Disjoin(id_={self.id})"


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


class Disjoin:
    def __init__(self):
        self.mapping = dict()

    def find(self, idx: int):
        if idx not in self.mapping:
            self.mapping[idx] = idx

        if self.mapping[idx] == idx:
            return idx

        self.mapping[idx] = self.find(self.mapping[idx])
        return self.mapping[idx]

    def test(self, a: int, b: int):
        a_leader = self.find(a)
        b_leader = self.find(b)
        if a_leader == b_leader:
            return True
        return False

    def merge(self, a: int, b: int):
        a_leader = self.find(a)
        b_leader = self.find(b)
        if a_leader != b_leader:
            self.mapping[a_leader] = b_leader


n, m = map(int, input().split())
# lst = [i for i in range(n + 1)]
dj = Disjoin()
for _ in range(m):
    z, x, y = map(int, input().split())

    if z == 1:
        dj.merge(x, y)
    else:
        if dj.test(x, y):
            print("Y")
        else:
            print("N")
