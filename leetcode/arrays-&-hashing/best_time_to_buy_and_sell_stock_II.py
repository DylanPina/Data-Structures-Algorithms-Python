from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            cur, prev = prices[i], prices[i - 1]
            if cur > prev:
                profit += cur - prev
        return profit
