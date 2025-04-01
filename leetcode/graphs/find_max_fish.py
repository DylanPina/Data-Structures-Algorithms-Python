from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr: int, sc: int) -> int:
            q = deque([(sr, sc)])
            fish = 0

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    fish += grid[r][c]
                    grid[r][c] = 0

                    for dr, dc in dirs:
                        nr, nc = dr + r, dc + c

                        if min(nr, nc) < 0 or nr == M or nc == N or grid[nr][nc] == 0:
                            continue

                        q.append((nr, nc))

            return fish

        max_fish = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] != 0:
                    max_fish = max(max_fish, bfs(r, c))

        return max_fish
