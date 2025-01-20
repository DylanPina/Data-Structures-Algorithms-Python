from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r: int, c: int) -> int:
            if min(r, c) < 0 or r == M or c == N or grid[r][c] or (r, c) in visited:
                return 0

            if r == M - 1 and c == N - 1:
                return 1

            visited.add((r, c))
            paths = 0
            for dr, dc in directions:
                paths += dfs(r + dr, c + dc)
            visited.remove((r, c))
            return paths

        return dfs(0, 0)
