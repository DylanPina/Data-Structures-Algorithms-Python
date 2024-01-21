from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.dp(obstacleGrid)

    def backtrack(self, obstacleGrid: List[List[int]], r: int, c: int) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if r == m or c == n or obstacleGrid[r][c] == 1:
            return 0
        if r == m - 1 and c == n - 1:
            return 1

        return self.backtrack(obstacleGrid, r + 1, c) + self.backtrack(
            obstacleGrid, r, c + 1
        )

    def memoization(
        self, obstacleGrid: List[List[int]], r: int, c: int, cache: List[List[int]]
    ) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if r == m or c == n or obstacleGrid[r][c] == 1:
            return 0
        if r == m - 1 and c == n - 1:
            return 1
        if cache[r][c] > 0:
            return cache[r][c]

        cache[r][c] = self.memoization(
            obstacleGrid, r + 1, c, cache
        ) + self.memoization(obstacleGrid, r, c + 1, cache)
        return cache[r][c]

    def dp(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[n - 1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]


sol = Solution()

print(sol.backtrack([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 0, 0))
print(sol.backtrack([[0, 1], [0, 0]], 0, 0))

print(
    sol.memoization(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]], 0, 0, [[0] * 3 for i in range(3)]
    )
)
print(sol.memoization([[0, 1], [0, 0]], 0, 0, [[0] * 3 for i in range(3)]))

print(sol.dp([[0, 0], [1, 1], [0, 0]]))
print(sol.dp([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
