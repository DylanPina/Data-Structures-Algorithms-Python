from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp_prices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if (new_price := prices[s] + p) < tmp_prices[d]:
                    tmp_prices[d] = new_price
            prices = tmp_prices

        return -1 if prices[dst] == float("inf") else prices[dst]
