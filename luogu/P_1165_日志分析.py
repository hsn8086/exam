from dataclasses import dataclass


@dataclass
class Item:
    id: int
    mass: int


que: list[Item] = [Item(0, 0)]
cnt = 0
for _ in range(int(input())):
    cmd = tuple(map(int, input().split()))

    if cmd[0] == 0:
        cnt += 1
        mass = cmd[1]
        if mass > que[-1].mass:
            que.append(Item(cnt, mass))
    elif cmd[0] == 1:
        if que[-1].id == cnt:
            que.pop(-1)
        cnt -= 1
    elif cmd[0] == 2:
        print(que[-1].mass)
