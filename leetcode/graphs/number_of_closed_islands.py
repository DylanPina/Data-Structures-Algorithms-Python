from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        closedIslands = 0

        def bfs(r: int, c: int) -> bool:
            q = deque([(r, c)])
            isClosed = True

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    grid[r][c] = -1

                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) < 0 or nr == M or nc == N:
                            isClosed = False
                        elif grid[nr][nc] == 0:
                            q.append((nr, nc))

            return isClosed

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0:
                    closedIslands += bfs(r, c)

        return closedIslands
