from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def intToPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            r = n - 1 - r
            return r, c

        q = deque([(1, 0)])
        visit = set()

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                if nextSquare == n * n:
                    return moves + 1

                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append((nextSquare, moves + 1))

        return -1
