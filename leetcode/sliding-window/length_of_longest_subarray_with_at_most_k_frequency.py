from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = l = 0

        for r in range(len(nums)):
            count[nums[r]] += 1

            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, (r - l) + 1)
        return res
