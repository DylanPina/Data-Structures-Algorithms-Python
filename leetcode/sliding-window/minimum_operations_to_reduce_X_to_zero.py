from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curSum = l = 0
        maxWindow = -1

        for r in range(len(nums)):
            curSum += nums[r]
            while l <= r and curSum > target:
                curSum -= nums[l]
                l += 1

            if curSum == target:
                maxWindow = max(maxWindow, r - l + 1)

        return -1 if maxWindow == -1 else len(nums) - maxWindow
