from math import prod
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = prod(nums)

        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
