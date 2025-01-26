from typing import List


class Solution:
    def countSubIslands(self, g1: List[List[int]], g2: List[List[int]]) -> int:
        M, N = len(g1), len(g1[0])

        def dfs(r: int, c: int) -> bool:
            # Boundary or visited checks
            if min(r, c) < 0 or r >= M or c >= N or not g2[r][c]:
                return True

            # If g2 has land but g1 does not, this is not a sub-island
            if g2[r][c] and not g1[r][c]:
                return False

            # Mark the cell in g2 as visited
            g2[r][c] = 0

            # Initialize validity of the current island
            isSubIsland = True

            # Check all four directions and combine their validity
            isSubIsland &= dfs(r - 1, c)
            isSubIsland &= dfs(r + 1, c)
            isSubIsland &= dfs(r, c - 1)
            isSubIsland &= dfs(r, c + 1)

            return isSubIsland

        subIslands = 0
        for r in range(M):
            for c in range(N):
                if g1[r][c] and g2[r][c]:  # Start DFS only from unvisited land in g2
                    if dfs(r, c):  # Check if the entire island is a sub-island
                        subIslands += 1

        return subIslands
