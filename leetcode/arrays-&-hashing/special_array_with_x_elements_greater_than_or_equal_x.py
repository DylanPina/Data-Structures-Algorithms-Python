from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i, prev = 0, -1
        while i < len(nums):
            total_right = len(nums) - i
            if nums[i] == total_right or (prev < total_right < nums[i]):
                return total_right

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            prev = nums[i]
            i += 1
        return -1
