import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}

        res = 0
        pq = [(0, 0, 0)]  # (effort, row, col)
        visited = set([(0, 0)])

        while pq:
            for _ in range(len(pq)):
                effort, r, c = heapq.heappop(pq)

                res = max(res, effort)
                if (r, c) == (ROWS - 1, COLS - 1):
                    return res

                visited.add((r, c))

                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c

                    if (
                        min(nr, nc) < 0
                        or nr >= ROWS
                        or nc >= COLS
                        or (nr, nc) in visited
                    ):
                        continue

                    heapq.heappush(pq, (abs(heights[r][c] - heights[nr][nc]), nr, nc))

        return -1
