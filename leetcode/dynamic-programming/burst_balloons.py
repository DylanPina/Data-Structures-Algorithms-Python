from typing import Dict, List, Tuple


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return self.dp(nums)

    def dp(self, nums: List[int]) -> int:
        dp: Dict[Tuple[int, int], int] = {}

        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            dp[(left, right)] = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                dp[(left, right)] = max(dp[(left, right)], coins)
            return dp[(left, right)]

        return dfs(1, len(nums) - 2)
