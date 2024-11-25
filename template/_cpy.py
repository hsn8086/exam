import sys


class Cin:
    def __init__(self, loc):
        self.loc = loc
        self.stdin = []
        ...

    def __rshift__(self, other):
        if not self.stdin:
            self.stdin = sys.stdin.readline().split()
        self.loc[other] = type(self.loc[other])(self.stdin.pop(0))
        return self


class Cout:
    def __init__(self, loc):
        self.loc = loc

    def __lshift__(self, other):
        if other in self.loc:
            sys.stdout.write(str(self.loc[other]))
        else:
            sys.stdout.write(str(other))
        return self


cin = Cin(locals())
cout = Cout(locals())
endl = "\n"

# n,q=map(int,input().split())
q = int()
n = int()
cin >> "n" >> "q"
d = {}
for _ in range(q):
    op = str()
    cin >> "op"
    if op == "1":
        i, j, k = int(), int(), int()
        cin >> "i" >> "j" >> "k"
        d[(i, j)] = k
    else:
        i, j = int(), int()
        cin >> "i" >> "j"
        cout << (d.get((i, j), 0)) << endl
