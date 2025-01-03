from typing import List
from heapq import heappop, heappush, heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            s1, s2 = heappop(stones), heappop(stones)
            if s1 != s2:
                heappush(stones, s1 - s2)
        return abs(stones[0]) if stones else 0
