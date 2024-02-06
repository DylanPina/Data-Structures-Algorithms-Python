from typing import Dict, Tuple


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.dp(s)

    def dp(self, s: str) -> int:
        s_reverse = s[::-1]
        N = len(s)

        prev_row = [0] * (N + 1)

        for i in range(N - 1, -1, -1):
            cur_row = [0] * (N + 1)
            for j in range(N - 1, -1, -1):
                if s[i] == s_reverse[j]:
                    cur_row[j] = 1 + prev_row[j + 1]
                else:
                    cur_row[j] = max(cur_row[j + 1], prev_row[j])
            prev_row = cur_row

        return prev_row[0]

    def memoization(self, s: str) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if i < 0 or j == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                length = 1 if i == j else 2
                cache[(i, j)] = length + dfs(i - 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
            return cache[(i, j)]

        for i in range(len(s)):
            dfs(i, i)
            dfs(i, i + 1)

        return max(cache.values())


sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))
