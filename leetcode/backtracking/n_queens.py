from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        col, pos_diag, neg_diag = set(), set(), set()

        def backtrack(r: int) -> None:
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or r + c in pos_diag or r - c + n in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c + n)
                board[r][c] = "Q"
                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c + n)
                board[r][c] = "."

        backtrack(0)
        return res
