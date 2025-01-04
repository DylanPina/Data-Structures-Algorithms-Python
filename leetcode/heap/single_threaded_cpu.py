from typing import List
from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        T = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        res, heap = [], []

        time, _, _ = T[0]
        i = 0
        while i < len(T) or heap:
            while i < len(T) and time >= T[i][0]:
                _, pt, idx = T[i]
                heappush(heap, (pt, idx))
                i += 1

            if not heap:
                time = T[i][0]
            else:
                pt, idx = heappop(heap)
                time += pt
                res.append(idx)

        return res
