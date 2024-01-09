from typing import Dict, List, Tuple


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.optimal(amount, coins)

    def optimal(self, amount: int, coins: List[int]) -> int:
        prev_row = [0] * (amount + 1)
        prev_row[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            cur_row = [0] * (amount + 1)
            cur_row[0] = 1

            for a in range(1, amount + 1):
                cur_row[a] += prev_row[a]
                if a - coins[i] >= 0:
                    cur_row[a] += cur_row[a - coins[i]]
            prev_row = cur_row
        return prev_row[amount]

    def dp(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1)] * (amount + 1)
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

    def backtrack(self, amount: int, coins: List[int]) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(i: int, a: int) -> int:
            if a == amount:
                return 1
            elif i == len(coins) or a > amount:
                return 0

            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)


sol = Solution()

print(sol.change(5, [1, 2, 5]))
print(sol.change(3, [2]))
print(sol.change(10, [10]))
