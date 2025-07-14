inf = 1 << 70


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        dp_p = [(0, -inf)] * len(matrix[0])
        dp_n = [(0, inf)] * len(matrix[0])
        ans = 0
        for line in matrix:
            now_p = [(0, -inf)]
            now_n = [(0, inf)]
            for i, v in enumerate(line):
                cnt_p, v_p = max(
                    [(0, v), *filter(lambda t: t[1] > v, (now_p[-1], dp_p[i]))]
                )
                cnt_n, v_n = max(
                    [(0, v), *filter(lambda t: t[1] < v, (now_n[-1], dp_n[i]))]
                )
                now_p.append((cnt_p + 1, v))

                now_n.append((cnt_n + 1, v))

            dp_n = now_n[1:]
            dp_p = now_p[1:]
            ans = max(*map(lambda t: t[0], dp_n), *map(lambda t: t[0], dp_p), ans)
            print(dp_n, dp_p)
        return ans


print(Solution().longestIncreasingPath([[7,8,9],[9,7,6],[7,2,3]]))
