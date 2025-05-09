import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(x_i: int, y_i: int, x_j: int, y_j: int) -> int:
            return abs(x_i - x_j) + abs(y_i - y_j)

        adj = defaultdict(list)
        for i in range(len(points)):
            x_i, y_i = points[i]
            for j in range(len(points)):
                x_j, y_j = points[j]
                dist = manhattan_distance(x_i, y_i, x_j, y_j)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        res = 0
        min_heap = []
        for j, d_j in adj[0]:
            heapq.heappush(min_heap, (d_j, j))
        visit = set()

        while len(visit) < len(points):
            d_i, i = heapq.heappop(min_heap)

            if i in visit:
                continue

            res += d_i
            visit.add(i)

            for j, d_j in adj[i]:
                if j not in visit:
                    heapq.heappush(min_heap, (d_j, j))

        return res if len(visit) == len(points) else -1
