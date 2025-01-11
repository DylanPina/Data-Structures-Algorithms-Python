from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        maxHeap = sorted([(e, s) for e, s in zip(efficiency, speed)], reverse=True)
        minHeap = []
        res = curSpeed = 0

        for e, s in maxHeap:
            if len(minHeap) == k:
                curSpeed -= heappop(minHeap)
            curSpeed += s
            heappush(minHeap, s)
            res = max(res, e * curSpeed)

        return res % (10**9 + 7)
