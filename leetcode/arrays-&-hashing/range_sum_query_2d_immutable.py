from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.prefix = [[] * self.COLS for _ in range(self.ROWS)]

        for r in range(self.ROWS):
            sum = 0
            for c in range(self.COLS):
                sum += matrix[r][c]
                self.prefix[r][c] = sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            left = self.prefix[row][col1 - 1] if col1 > 0 else 0
            right = self.prefix[row][col2]
            sum += right - left
        return sum