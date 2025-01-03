from typing import List
from heapq import heappush, heappop


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            bricks -= diff
            heappush(maxHeap, -diff)

            if bricks < 0:
                if not ladders:
                    return i
                ladders -= 1
                bricks += -heappop(maxHeap)

        return len(heights) - 1
