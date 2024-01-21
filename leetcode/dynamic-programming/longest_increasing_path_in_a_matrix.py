from typing import Dict, List, Tuple


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp: Dict[Tuple[int, int], int] = {}

        def dfs(r: int, c: int, prev: int) -> int:
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prev:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())


sol = Solution()
print(sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(sol.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
