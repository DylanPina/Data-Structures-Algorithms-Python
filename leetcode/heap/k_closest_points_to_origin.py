from typing import List
from heapq import nsmallest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)
