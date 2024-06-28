from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue

            newCount = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    newCount[n] = c - 1
            count = newCount

        res = []
        for n, c in count.items():
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
