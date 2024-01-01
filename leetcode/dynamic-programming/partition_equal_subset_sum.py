import copy
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set([0])

        for i in range(len(nums) - 1, -1, -1):
            next_dp = copy.copy(dp)
            for t in dp:
                if t + nums[i] == target:
                    return True
                next_dp.add(t + nums[i])
            dp = next_dp

        return False
