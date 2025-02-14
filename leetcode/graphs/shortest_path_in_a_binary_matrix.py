from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        if g[0][0] == 1:
            return -1

        M, N = len(g), len(g[0])
        neighbors = [
            (1, 0),
            (1, 1),
            (-1, -1),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, -1),
            (-1, 1),
        ]
        visited = set([(0, 0)])
        q = deque([(0, 0)])
        length = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == M - 1 and c == N - 1:
                    return length

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < M
                        and 0 <= nc < N
                        and not g[nr][nc]
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

            length += 1

        return -1
