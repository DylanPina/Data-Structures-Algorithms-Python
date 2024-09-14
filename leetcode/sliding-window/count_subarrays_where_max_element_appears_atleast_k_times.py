from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum, maxCount = max(nums), 0
        res = l = 0

        for r in range(len(nums)):
            if nums[r] == maxNum:
                maxCount += 1

            while maxCount > k or (maxCount == k and nums[l] != maxNum):
                if nums[l] == maxNum:
                    maxCount -= 1
                l += 1
            if maxCount == k:
                res += l + 1
        return res
