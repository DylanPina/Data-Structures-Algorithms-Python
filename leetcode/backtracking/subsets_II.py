from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, cur_subset = [], []

        def helper(i: int) -> None:
            if i == len(nums):
                res.append(cur_subset.copy())
                return

            cur_subset.append(nums[i])
            helper(i + 1)

            cur_subset.pop()
            while i + 1 != len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1)

        nums.sort()
        helper(0)
        return res
