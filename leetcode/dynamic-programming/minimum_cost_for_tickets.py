from collections import defaultdict
from typing import Dict, List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.dp(days, costs)

    def dp(self, days: List[int], costs: List[int]) -> int:
        dp: Dict[int, int | float] = defaultdict(int)

        for i in range(len(days) - 1, -1, -1):
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])

        return int(dp[0])

    def memoization(self, days: List[int], costs: List[int]) -> int:
        dp: Dict[int, int | float] = {}

        def dfs(i: int) -> int:
            if i == len(days):
                return 0
            if i in dp:
                return int(dp[i])

            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return int(dp[i])

        return dfs(0)


sol = Solution()
print(sol.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
