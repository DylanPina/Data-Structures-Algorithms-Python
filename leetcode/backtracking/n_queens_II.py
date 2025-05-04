class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [["."] * n for _ in range(n)]
        col, pos_diag, neg_diag = set(), set(), set()

        def backtrack(r: int) -> None:
            nonlocal res

            if r == n:
                res += 1
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
