for tc in range(int(input())):
    n, m, d = map(int, input().split())
    levels = []
    for i in range(n):
        inp = input()
        for j in range(m):
            if inp[j] == "X":
                if i > len(levels) - 1:
                    levels.append([])

                levels[-1].append([j, 0, 0])
                if i == n - 1:
                    levels[-1][-1][1] = 1

    for lev_i, level in enumerate(levels[::-1]):
        # h
        for i, v in enumerate(level):
            x, cnt, cnt_h = v
            # down
            for j in range(1, d + 1):
                idx = lev_i - j
                if idx < 0:
                    break
                d_level = levels[-idx - 1]
                # left
                for k in range(max(1, d - j + 2)):
                    if (
                        i - k < 0
                        or i - k >= len(d_level)
                        or x - d_level[i - k][0] >= d - j
                    ):
                        break
                    cnt += d_level[i - k - 1][1] + d_level[i - k - 1][2]
                # right
                for k in range(max(1, d - j + 1)):
                    if (
                        i + k + 1 < 0
                        or i + k + 1 >= len(d_level)
                        or d_level[i + k + 1][0] - x >= d - j
                    ):
                        break
                    cnt += d_level[i + k + 1][1] + d_level[i + k + 1][2]

                level[i][1] += cnt

            # level
            # left
            for j in range(d):
                if i - j - 1 < 0 or x - level[i - j - 1][0] > d:
                    break
                # if lev_i == 0:
                #     cnt_h += 1
                # else:
                #     cnt_h += level[i - j - 1][1]
                cnt_h += level[i - j - 1][1]
            # right
            for j in range(d):
                if i + j + 1 >= len(level) or level[i + j + 1][0] - x > d:
                    break
                # if lev_i == 0:
                #     cnt_h += 1
                # else:
                #     cnt_h += level[i + j + 1][1]
                cnt_h += level[i + j + 1][1]
            level[i][2] += cnt_h

    print("tc", tc + 1)
    print(*levels, sep="\n")
