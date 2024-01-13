from typing import List, Dict, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache: Dict[Tuple[int, bool], int] = {}

        def dfs(i: int, buy: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, buy) in cache:
                return cache[(i, buy)]

            if buy:
                cache[(i, buy)] = max(dfs(i + 1, not buy) - prices[i], dfs(i + 1, buy))
            else:
                cache[(i, buy)] = max(dfs(i + 2, not buy) + prices[i], dfs(i + 1, buy))
            return cache[(i, buy)]

        return dfs(0, True)


sol = Solution()

print(sol.maxProfit([1, 2, 3, 0, 2]))
print(sol.maxProfit([1]))
