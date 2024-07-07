from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        nums.sort()
        for r in range(0, len(nums), 3):
            if nums[r + 2] - nums[r] > k:
                return []
            res.append(nums[r : r + 3])
        return res
