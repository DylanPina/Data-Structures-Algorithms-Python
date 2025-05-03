from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise_or = reduce(lambda x, y: x | y, nums)

        def backtrack(i: int, sum: int) -> None:
            if i == len(nums):
                return sum == max_bitwise_or

            return backtrack(i + 1, sum) + backtrack(i + 1, sum | nums[i])

        return backtrack(0, 0)
