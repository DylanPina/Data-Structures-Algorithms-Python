from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int, i=0) -> bool:
            if i == len(word):
                return True

            if board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if min(nr, nc) < 0 or nr == M or nc == N or board[nr][nc] == "#":
                    continue

                if dfs(nr, nc, i + 1):
                    return True

            board[r][c] = temp
            return False

        for r in range(M):
            for c in range(N):
                if board[r][c] == word[0] and dfs(r, c):
                    return True
        return False
