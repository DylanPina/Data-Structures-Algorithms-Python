from collections import deque
from typing import List


class Solution:
    def shortestPath(self, g: List[List[int]]) -> int:
        M, N = len(g), len(g[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        length = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == M - 1 and c == N - 1:
                    return length

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if (
                        0 <= nr < M
                        and 0 <= nc < N
                        and g[nr][nc] == 0
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            length += 1

        return -1
