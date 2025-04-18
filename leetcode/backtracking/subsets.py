from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, cur_subset = [], []

        def helper(i: int) -> None:
            if i == len(nums):
                res.append(cur_subset.copy())
                return

            cur_subset.append(nums[i])
            helper(i + 1)

            cur_subset.pop()
            helper(i + 1)

        helper(0)
        return res
