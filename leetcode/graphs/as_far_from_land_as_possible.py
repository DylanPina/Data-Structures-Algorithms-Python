from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        distances = [[-1] * N for _ in range(M)]
        maxDistance = 0

        q = deque()
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append((r, c))
                    distances[r][c] = 0

        if not q or len(q) == M * N:
            return -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < M
                        and 0 <= nc < N
                        and grid[nr][nc] == 0
                        and distances[nr][nc] == -1
                    ):
                        distances[nr][nc] = distances[r][c] + 1
                        maxDistance = max(maxDistance, distances[nr][nc])
                        q.append((nr, nc))

        return maxDistance
