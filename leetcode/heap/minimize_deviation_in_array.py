from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap, heapMax = [], 0
        for n in nums:
            tmp = n
            while n % 2 == 0:
                n //= 2
            minHeap.append((n, max(tmp, 2 * n)))
            heapMax = max(heapMax, n)

        res = float("inf")
        heapify(minHeap)
        while len(minHeap) == len(nums):
            n, nMax = heappop(minHeap)
            res = min(res, heapMax - n)

            if n < nMax:
                heappush(minHeap, (n * 2, nMax))
                heapMax = max(heapMax, n * 2)

        return int(res)
