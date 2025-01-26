from typing import List


class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        M, N = len(g), len(g[0])
        perimeter = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r: int, c: int) -> None:
            nonlocal perimeter
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nr > M - 1 or nc > N - 1 or not g[nr][nc]:
                    perimeter += 1
                elif (nr, nc) not in visited:
                    dfs(nr, nc)

        for r in range(M):
            for c in range(N):
                if g[r][c]:
                    dfs(r, c)
                    return perimeter
        return 0
