from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7

        res = 0
        r = len(nums) - 1
        for i, left in enumerate(nums):
            while left + nums[r] > target and i <= r:
                r -= 1
            if i <= r:
                res += 2 ** (r - i)
        return res % mod
