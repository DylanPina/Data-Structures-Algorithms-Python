from typing import List


class Solution:
    def checkMove(
        self, board: List[List[str]], rMove: int, cMove: int, color: str
    ) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            [1, 1],
            [-1, -1],
            [1, -1],
            [-1, 1],
        ]

        board[rMove][cMove] = color

        def legal(r: int, c: int, dr: int, dc: int, color: str) -> bool:
            nr, nc = dr + r, dc + c
            length = 1

            while 0 <= nr < ROWS and 0 <= nc < COLS:
                length += 1
                if board[nr][nc] == ".":
                    return False
                if board[nr][nc] == color:
                    return length >= 3
                nr += dr
                nc += dc
            return False

        for dr, dc in dirs:
            if legal(rMove, cMove, dr, dc, color):
                return True
        return False
