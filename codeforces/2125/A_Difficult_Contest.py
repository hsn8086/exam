for _ in range(int(input())):
    inp = input()
    text = []
    cnt = 0

    for i in inp:
        if i == "T":
            cnt += 1
        else:
            text.append(i)

    print("T" * cnt + "".join(text))
