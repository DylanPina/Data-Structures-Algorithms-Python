from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(m, n)

    def backtrack(self, m: int, n: int, r: int, c: int) -> int:
        if r == m or c == n:
            return 0
        if r == m - 1 and c == n - 1:
            return 1

        return self.backtrack(m, n, r + 1, c) + self.backtrack(m, n, r, c + 1)

    def memoization(
        self, m: int, n: int, r: int, c: int, cache: List[List[int]]
    ) -> int:
        if r == m or c == n:
            return 0
        if r == m - 1 and c == n - 1:
            return 1
        if cache[r][c] > 0:
            return cache[r][c]

        return self.memoization(m, n, r + 1, c, cache) + self.memoization(
            m, n, r, c + 1, cache
        )

    def dp(self, m: int, n: int) -> int:
        prev_row = [0] * n

        for r in range(m - 1, -1, -1):
            cur_row = [0] * n
            cur_row[n - 1] = 1

            for c in range(n - 2, -1, -1):
                cur_row[c] = prev_row[c] + cur_row[c + 1]
            prev_row = cur_row

        return prev_row[0]


sol = Solution()

print(sol.backtrack(3, 7, 0, 0))
print(sol.backtrack(3, 2, 0, 0))

print(sol.memoization(3, 7, 0, 0, [[0] * 7 for _ in range(3)]))
print(sol.memoization(3, 2, 0, 0, [[0] * 2 for _ in range(3)]))

print(sol.dp(3, 7))
print(sol.dp(3, 2))
