from typing import Dict, List, Tuple


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dp(profit, weight, capacity)

    def dp(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prev_row = [0] * (capacity + 1)

        for r in range(len(weight)):
            cur_row = [0] * (capacity + 1)
            for c in range(capacity + 1):
                skip = prev_row[c]
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + prev_row[c - weight[r]]
                cur_row[c] = max(skip, include)
            prev_row = cur_row

        return prev_row[capacity]

    def memoization(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, remaining: int) -> int:
            if i == len(profit):
                return 0

            if (i, remaining) in cache:
                return cache[(i, remaining)]

            skip = dfs(i + 1, remaining)
            include = 0
            if remaining - weight[i] >= 0:
                include = profit[i] + dfs(i + 1, remaining - weight[i])

            cache[(i, remaining)] = max(skip, include)
            return cache[(i, remaining)]

        return dfs(0, capacity)

    def backtrack(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i: int, remaining: int) -> int:
            if i == len(profit):
                return 0

            skip = dfs(i + 1, remaining)
            if remaining - weight[i] >= 0:
                include = profit[i] + dfs(i + 1, remaining - weight[i])
                return max(skip, include)
            return skip

        return dfs(0, capacity)


sol = Solution()
print(sol.maximumProfit([4, 4, 7, 1], [5, 2, 3, 1], 8))
