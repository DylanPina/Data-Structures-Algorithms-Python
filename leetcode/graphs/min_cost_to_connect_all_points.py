from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:  # Edge case
            return 0

        # Build adjacency list using indices for clarity
        adj = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        # Prim's Algorithm: Min-Heap to store (weight, point)
        minHeap = [(0, 0)]  # Start with point 0
        visit = set()
        res = 0

        while len(visit) < len(points):
            weight, curr = heappop(minHeap)
            if curr in visit:
                continue

            visit.add(curr)
            res += weight

            for nextWeight, nextPoint in adj[curr]:
                if nextPoint not in visit:
                    heappush(minHeap, (nextWeight, nextPoint))

        return res
