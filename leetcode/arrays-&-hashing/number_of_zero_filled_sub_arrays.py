from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = count = 0
        for num in nums:
            if not num:
                count += 1
            else:
                count = 0
            res += count
        return res
