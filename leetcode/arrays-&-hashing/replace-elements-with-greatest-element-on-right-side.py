from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        cur_max = -1
        for i in range(len(arr) - 1, -1, -1):
            res.insert(0, cur_max)
            cur_max = max(arr[i], cur_max)
        return res
