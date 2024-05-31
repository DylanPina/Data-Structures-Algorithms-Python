from collections import defaultdict
from typing import List
from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        occurences = defaultdict(int)
        for num in nums:
            occurences[num] += 1

        res = 0
        for count in occurences.values():
            res += comb(count, 2)
        return res
