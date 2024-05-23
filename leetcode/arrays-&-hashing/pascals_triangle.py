from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            cur_row = []
            for i in range(row_num + 1):
                if i == 0 or i == row_num:
                    cur_row.append(1)
                else:
                    prev_row = triangle[row_num]
                    cur_row.append(
                        prev_row[i - 1] + prev_row[i] if i < len(prev_row) else 0
                    )
            triangle.append(cur_row)
        return triangle
