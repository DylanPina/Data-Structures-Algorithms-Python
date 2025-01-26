from collections import deque
from typing import List, Tuple


class Solution:
    def islandsAndTreasure(self, g: List[List[int]]) -> None:
        if not g or not g[0]:
            return

        M, N = len(g), len(g[0])

        # Find the treasure:
        treasureLocations = []
        for r in range(M):
            for c in range(N):
                if g[r][c] == 0:
                    treasureLocations.append((r, c))

        if not len(treasureLocations):
            return

        def bfs(treasure: Tuple[int, int]) -> None:
            q = deque([treasure])
            visited = set()
            distance = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    if (r, c) in visited:
                        continue

                    if distance < g[r][c]:
                        g[r][c] = distance
                    visited.add((r, c))

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if (
                            0 <= nr < M
                            and 0 <= nc < N
                            and g[nr][nc] != -1
                            and (nr, nc) not in visited
                        ):
                            q.append((nr, nc))
                distance += 1

        for r, c in treasureLocations:
            bfs((r, c))
