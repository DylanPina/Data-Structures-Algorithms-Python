from heapq import heappop, heappush
from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        res = float("inf")
        pairs = sorted([(w / q, q) for w, q in zip(wage, quality)])

        maxHeap = []  # Qualities
        totalQuality = 0
        for rate, q in pairs:
            heappush(maxHeap, -q)
            totalQuality += q

            if len(maxHeap) > k:
                totalQuality += heappop(maxHeap)

            if len(maxHeap) == k:
                res = min(res, totalQuality * rate)

        return res
