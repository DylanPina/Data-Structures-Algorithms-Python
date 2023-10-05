from typing import List
from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.append((r, c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist

                visited.append((r, c))
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    row, col = r + dr, c + dc
                    if (not row in range(ROWS) or
                        not col in range(COLS) or
                        (row, col) in visited or
                            rooms[row][col] == -1):
                        continue
                    queue.append((row, col))
                dist += 1
