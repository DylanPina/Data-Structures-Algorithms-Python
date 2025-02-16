from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        found = False
        q = deque()

        # Helper function to perform DFS and find the first island
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))  # Add boundary of first island to queue
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Locate the first island and mark it
        for r in range(ROWS):
            if found:
                break
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break  # Break out of both loops

        # Perform BFS to find the shortest bridge
        bridgeLen = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1:
                            return bridgeLen  # Found the second island
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2  # Mark visited water
                            q.append((nr, nc))

            bridgeLen += 1

        return -1
