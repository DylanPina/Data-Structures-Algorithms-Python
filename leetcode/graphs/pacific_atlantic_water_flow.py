from typing import List


class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        M, N = len(h), len(h[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()

        def dfs(r: int, c: int, visit: set) -> None:
            if (r, c) in visit:
                return

            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    min(nr, nc) >= 0
                    and nr < M
                    and nc < N
                    and (nr, nc) not in visit
                    and h[nr][nc] >= h[r][c]
                ):
                    dfs(nr, nc, visit)

        for r in range(M):
            dfs(r, 0, pacific)
        for c in range(N):
            dfs(0, c, pacific)

        for r in range(M):
            dfs(r, N - 1, atlantic)
        for c in range(N):
            dfs(M - 1, c, atlantic)

        return list(pacific & atlantic)
