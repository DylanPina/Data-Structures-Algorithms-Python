from collections import deque


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = [[False] * N for _ in range(M)]
        q = deque()

        land, borderLand = 0, 0
        for r in range(M):
            for c in range(N):
                land += grid[r][c]
                if grid[r][c] == 1 and (r in (0, M - 1) or c in (0, N - 1)):
                    q.append((r, c))
                    visit[r][c] = True

        while q:
            r, c = q.popleft()
            borderLand += 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < M
                    and 0 <= nc < N
                    and grid[nr][nc] == 1
                    and not visit[nr][nc]
                ):
                    q.append((nr, nc))
                    visit[nr][nc] = True

        return land - borderLand
