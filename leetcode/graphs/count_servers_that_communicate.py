from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        row_cnt, col_cnt = [0] * M, [0] * N

        for r in range(M):
            for c in range(N):
                if grid[r][c]:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        res = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] and max(row_cnt[r], col_cnt[c]) > 1:
                    res += 1
        return res
