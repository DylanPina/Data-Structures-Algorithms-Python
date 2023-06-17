from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur =  board[r][c]
                if cur == '.': 
                    continue
                if (
                    cur in rows[r] or
                    cur in cols[c] or
                    cur in boxes[(r // 3, c // 3)]
                ): return False
                else:
                    rows[r].add(cur)
                    cols[c].add(cur)
                    boxes[(r // 3, c // 3)].add(cur)
        
        return True

