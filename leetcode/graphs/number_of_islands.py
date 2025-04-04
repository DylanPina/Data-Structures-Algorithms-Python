from typing import List


class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        M, N = len(g), len(g[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        def dfs(r: int, c: int) -> None:
            if min(r, c) < 0 or r == M or c == N or g[r][c] == "0":
                return

            g[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(M):
            for c in range(N):
                if g[r][c] == "0":
                    continue
                dfs(r, c)
                islands += 1

        return islands
