class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
                    
        return islands
