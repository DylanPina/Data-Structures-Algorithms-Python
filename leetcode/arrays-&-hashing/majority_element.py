from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = defaultdict()
        res = nums[0]
        for num in nums:
            occurences[num] += 1
            res = num if occurences[num] > occurences[res] else res
        return res
