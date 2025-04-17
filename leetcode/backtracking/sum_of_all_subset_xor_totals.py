from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = cur = 0

        def dfs(i: int) -> None:
            nonlocal total, cur

            if i == len(nums):
                total += cur
                return

            cur ^= nums[i]
            dfs(i + 1)

            cur ^= nums[i]
            dfs(i + 1)

        dfs(0)
        return total
