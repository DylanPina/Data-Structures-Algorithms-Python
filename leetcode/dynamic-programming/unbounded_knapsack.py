from typing import Dict, List, Tuple


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dp(profit, weight, capacity)

    def dp(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prev_row = [0] * (capacity + 1)

        for i in range(len(profit)):
            cur_row = [0] * (capacity + 1)
            for j in range(1, capacity + 1):
                skip = prev_row[j]

                include = 0
                new_capacity = j - weight[i]
                if new_capacity >= 0:
                    include = profit[i] + cur_row[new_capacity]
                cur_row[j] = max(skip, include)
            prev_row = cur_row

        return prev_row[capacity]

    def memoization(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, capacity: int) -> int:
            if i == len(weight) or capacity < 0:
                return 0
            if (i, capacity) in cache:
                return cache[(i, capacity)]

            skip = dfs(i + 1, capacity)

            include = 0
            new_capacity = capacity - weight[i]
            if new_capacity >= 0:
                include = profit[i] + dfs(i, new_capacity)
            cache[(i, capacity)] = max(skip, include)
            return cache[(i, capacity)]

        return dfs(0, capacity)

    def backtracking(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i: int, capacity: int) -> int:
            if i == len(weight) or capacity < 0:
                return 0

            skip = dfs(i + 1, capacity)

            include = 0
            new_capacity = capacity - weight[i]
            if new_capacity >= 0:
                include = profit[i] + dfs(i, new_capacity)
            return max(skip, include)

        return dfs(0, capacity)
