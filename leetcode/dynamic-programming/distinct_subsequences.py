from typing import Dict, Tuple


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.dp(s, t)

    def dp(self, s: str, t: str) -> int:
        prev_row = [0] * (len(t) + 1)
        prev_row[len(t)] = 1

        for r in range(len(s) - 1, -1, -1):
            cur_row = [0] * (len(t) + 1)
            cur_row[len(t)] = 1

            for c in range(len(t) - 1, -1, -1):
                if s[r] == t[c]:
                    cur_row[c] = prev_row[c] + prev_row[c + 1]
                else:
                    cur_row[c] = prev_row[c]
            prev_row = cur_row

        return prev_row[0]

    def memoization(self, s: str, t: str) -> int:
        dp: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)

            return dp[(i, j)]

        return dfs(0, 0)


sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))
