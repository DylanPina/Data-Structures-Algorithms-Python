from heapq import heappush, heappop
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heappush(min_heap, (r - l + 1, r))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]
