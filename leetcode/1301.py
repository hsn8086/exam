inf = 1 << 70


class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        dp = [(0, 1)] + [(-inf, -inf) for _ in range(len(board[0]) + 1)]
        for line in reversed(board):
            # print(dp)
            now = [(-inf, -inf)]
            for i, v in enumerate(reversed(line), 1):
                if v == "X":
                    now.append((-inf, -inf))
                    continue
                elif v in "SE":
                    v = 0
                max_ = -inf + 1
                max_cnt = 0

                for j, cnt in (dp[i - 1], dp[i], now[-1]):
                    if j > max_:
                        max_ = j
                        max_cnt = cnt
                    elif j == max_:
                        max_cnt += cnt
                now.append((max_ + int(v), max_cnt))
            dp = now
        return list(map(lambda x: max(x, 0) % (10**9 + 7), dp[-1]))


# print(Solution().pathsWithMaxScore(["E11", "XXX", "11S"]))
