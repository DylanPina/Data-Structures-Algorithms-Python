from typing import List

    
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = { i: float("inf") for i in range(n) }
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices.copy()
            for u, v, p in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u] + p < temp_prices[v]:
                    temp_prices[v] = prices[u] + p
            prices = temp_prices
        return -1 if prices[dst] == float("inf") else prices[dst]