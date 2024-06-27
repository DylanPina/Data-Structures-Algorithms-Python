class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]  # Flow
        for row in range(1, query_row + 1):
            cur_row = [float(0)] * (row + 1)
            for i in range(row):
                extra = prev_row[i] - 1
                if extra > 0:
                    extra_amount = 0.5 * extra
                    cur_row[i] += extra_amount
                    cur_row[i + 1] += extra_amount
            prev_row = cur_row
        return min(1, prev_row[query_glass])
