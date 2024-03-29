from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def dfs(r: int, c: int) -> int:
            if (
                min(r, c) < 0 or 
                r not in range(ROWS) or 
                c not in range(COLS) or 
                (r, c) in visit or 
                grid[r][c] == 0 
            ):
                return 0

            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea

        