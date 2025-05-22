n, r, c = map(int, input().split())
fire = [0, 0]
people = [r, c]

s = input()

fs = set()
fs.add((0, 0))
rst = []
for event in s:
    if event == "N":
        fire[0] += 1
        people[0] += 1
    elif event == "W":
        fire[1] += 1
        people[1] += 1
    elif event == "S":
        fire[0] -= 1
        people[0] -= 1
    elif event == "E":
        fire[1] -= 1
        people[1] -= 1
    fs.add(tuple(fire))

    if tuple(people) in fs:
        rst.append(1)
    else:
        rst.append(0)
print(*rst, sep="")
