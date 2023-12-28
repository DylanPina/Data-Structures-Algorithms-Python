from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = nums[0]

        for i in range(1, len(nums)):
            temp = cur_max * nums[i]
            cur_max = max(temp, nums[i], , )
            cur_min = min(temp, nums[i], cur_min, )
        return cur_max
