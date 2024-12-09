from rich.progress import track
count = 0
tap = 50
break_ = 30
for i in track(range(tap + 1)):
    for j in range(0, tap + 1 - i):
        for k in range(0, tap + 1 - i - j):
            for l_ in range(0, break_ + 1):
                for m in range(0, break_ + 1 - l_):
                    for n in range(0, break_ + 1 - l_ - m):
                        if (
                            0
                            < ((i + l_) * 500 + (j + m) * 200 + (k + n) * 100)
                            / ((tap + break_) * 500)
                            + (l_ * 100 + m * 75 + n * 50) / (break_ * 100 * 100)
                            - 0.114514
                            < 0.00001
                        ):
                            print(1)

print(count)
print(((i + l_) * 500 + (j + m) * 200 + (k + n) * 100)/ ((tap + break_) * 500)+(l_ * 100 + m * 75 + n * 50) / (break_ * 100 * 100))