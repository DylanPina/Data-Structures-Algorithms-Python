from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res, present = [], [0] * len(nums)
        for num in nums:
            present[num - 1] = 1
        for i in range(len(nums)):
            if present[i] == 0:
                res.append(i + 1)
        print(present)
        return res
