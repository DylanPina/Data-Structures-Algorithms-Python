from math import ceil
from typing import Dict, List, Tuple


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = ceil(stone_sum)
        dp: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, total: int) -> int:
            if total >= target or i == len(stones):
                return abs((total) - (stone_sum - total))
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return dp[(i, total)]

        return dfs(0, 0)
