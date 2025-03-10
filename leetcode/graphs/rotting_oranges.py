from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        M, N = len(g), len(g[0])
        time = 0
        rotting = deque()
        freshFruit = 0
        for r in range(M):
            for c in range(N):
                if g[r][c] == 2:
                    rotting.append((r, c))
                elif g[r][c] == 1:
                    freshFruit += 1

        if not freshFruit:
            return time

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while rotting:
            if not freshFruit:
                return time

            for _ in range(len(rotting)):
                r, c = rotting.popleft()

                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < M and 0 <= nc < N and g[nr][nc] == 1:
                        g[nr][nc] = 2
                        rotting.append((nr, nc))
                        freshFruit -= 1
            time += 1

        return -1
