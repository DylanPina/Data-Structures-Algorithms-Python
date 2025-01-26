from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, region: set) -> bool:
            region.add((r, c))
            visited.add((r, c))

            surrounded = True
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if min(nr, nc) < 0 or nr == M or nc == N:
                    return False

                if (nr, nc) not in region and board[nr][nc] == "O":
                    surrounded &= dfs(nr, nc, region)

            return surrounded

        def changeSurroundedRegion(region: set) -> None:
            for r, c in region:
                board[r][c] = "X"

        for r in range(M):
            for c in range(N):
                if (r, c) not in visited and board[r][c] == "O":
                    region = set()
                    if dfs(r, c, region):
                        changeSurroundedRegion(region)
