

import random
import subprocess
def check(a: list, x: int, y: int) -> int:
    for i in range(len(a)):
        if a[i]==a[i-1]:
            return False

    if a[x-1]==a[y-1]:
        return False
    return True
ntc=10
tc=""
for i in range(ntc):
    n=random.randint(2, 100)
    x=random.randint(1, n-1)
    y=random.randint(x, n)
    tc+=f"{n} {x} {y}\n"

op=subprocess.run(["python", "C_MEX_Cycle.py"], input=f"{ntc}\n"+tc, text=True, capture_output=True)
print()
rst=op.stdout.split("\n")
inp=tc.split("\n")[:-1]
for i in range(ntc):
    n, x, y=map(int, inp[i].split())
    a=list(map(int, rst[i].split()))
    if not a:
        continue
    try:
        assert check(a, x, y)
    except:
        print(n, x, y)
        print(a)
        print(check(a, x, y))
        break