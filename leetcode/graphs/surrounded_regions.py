from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if (
                not r in range(ROWS) or
                not c in range(COLS) or
                board[r][c] == "X" or
                board[r][c] == "T"
            ):
                return

            board[r][c] = "T"
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(r + dr, c + dc)

        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS - 1, i)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
