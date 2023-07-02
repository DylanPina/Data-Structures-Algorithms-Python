from typing import List

class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        max_prof, l = 0, 0

        for r in range(len(prices)):
            max_prof = max(max_prof, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
        return max_prof
