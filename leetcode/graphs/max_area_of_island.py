from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r: int, c: int) -> int:
            if min(r, c) < 0 or r == M or c == N or not grid[r][c]:
                return 0

            grid[r][c] = 0
            area = 0
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area + 1

        for r in range(M):
            for c in range(N):
                if not grid[r][c]:
                    continue
                res = max(res, dfs(r, c))

        return res
