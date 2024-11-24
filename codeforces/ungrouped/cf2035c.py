import math

num_of_tc = int(input())
for _ in range(num_of_tc):
    n = int(input())
    if n==5:
        print(5)
        print("2 1 3 4 5")
        continue
    nl = [i for i in range(1, n + 1)]
    rl = []
    if n % 2 == 0:
        c = int(math.log(n, 2))
        rl.append(nl.pop(-1))

        for i in range(c, 0, -1):
            nl.remove((2**i) - 1)
            rl.append((2**i) - 1)

            for j in nl[::-1]:
                if bin(j)[-i] == "1":
                    rl.append(j)
                    nl.remove(j)
                    break
    else:
        c = int(math.log(n, 2))
        rl.append(nl.pop(-1))
        for i in range(c, 0, -1):
            nl.remove((2**i) - 1)
            for j in nl[::-1]:
                if bin(j)[-i-1] == "1":
                    rl.append(j)
                    nl.remove(j)
                    break

            rl.append((2**i) - 1)
        for j in nl[::-1]:
                if bin(j)[-1] == "1":
                    rl.append(j)
                    nl.remove(j)
                    break
    rl += nl
    rst = 0
    for i, v in enumerate(rl[::-1]):

        if (i + 1) % 2 == 0:
            rst |= v
        else:
            rst &= v

    print(rst)
    print(" ".join(map(str, rl[::-1])))
