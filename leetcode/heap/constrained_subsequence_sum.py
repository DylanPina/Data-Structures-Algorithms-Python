from heapq import heappop, heappush
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        maxHeap = [(-nums[0], 0)]
        res = nums[0]

        for i in range(1, len(nums)):
            while i - maxHeap[0][1] > k:
                heappop(maxHeap)

            curMax = max(nums[i], nums[i] - maxHeap[0][0])
            res = max(res, curMax)
            heappush(maxHeap, (-curMax, i))

        return res
