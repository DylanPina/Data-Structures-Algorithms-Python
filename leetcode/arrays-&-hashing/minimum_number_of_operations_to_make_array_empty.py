from typing import List
from collections import Counter
from math import ceil


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res, count = 0, Counter(nums)
        for c in count.values():
            if c == 1:
                return -1
            res += ceil(c / 3)
        return res
