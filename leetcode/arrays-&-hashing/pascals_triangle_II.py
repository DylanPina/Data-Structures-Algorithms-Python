from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur, ans = 1, [1]
        for i in range(1, rowIndex + 1):
            cur *= (rowIndex + 1 - i) // i
            ans.append(cur) 
        return ans
