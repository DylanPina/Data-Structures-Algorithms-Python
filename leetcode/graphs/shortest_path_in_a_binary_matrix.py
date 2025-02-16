from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        if (ROWS - 1, COLS - 1) == (0, 0):
            return 1

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]

        q = deque([(0, 0)])
        visited = set()
        distance = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0
                        or nr >= ROWS
                        or nc >= COLS
                        or (nr, nc) in visited
                        or grid[nr][nc] != 0
                    ):
                        continue

                    if (nr, nc) == (ROWS - 1, COLS - 1):
                        return distance + 1

                    q.append((nr, nc))
                    visited.add((nr, nc))
            distance += 1

        return -1
