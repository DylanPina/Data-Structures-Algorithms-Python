from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int, visiting: set) -> int:
            visiting.add((r, c))
            gold = grid[r][c]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (
                    min(nr, nc) < 0
                    or nr == ROWS
                    or nc == COLS
                    or not grid[nr][nc]
                    or (nr, nc) in visiting
                ):
                    continue

                gold = max(gold, grid[r][c] + dfs(nr, nc, visiting))

            visiting.remove((r, c))
            return gold

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res = max(res, dfs(r, c, set()))
        return res
