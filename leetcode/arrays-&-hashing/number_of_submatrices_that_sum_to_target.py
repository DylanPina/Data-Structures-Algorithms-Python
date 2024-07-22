from typing import List
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        subSum = [[0] * (COLS + 1) for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                top = subSum[r - 1][c] if r > 0 else 0
                left = subSum[r][c - 1] if c > 0 else 0
                topLeft = subSum[r - 1][c - 1] if r > 0 and c > 0 else 0
                subSum[r][c] = matrix[r][c] + top + left - topLeft

        res = 0
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                count = defaultdict(int)
                count[0] = 1
                for c in range(COLS):
                    curSum = subSum[r2][c] - (subSum[r1 - 1][c] if r1 > 0 else 0)
                    diff = curSum - target
                    res += count[diff]
                    count[curSum] += 1
        return res
